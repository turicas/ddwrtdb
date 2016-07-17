#!/usr/bin/env python
# coding: utf-8

# Copyright 2016 Álvaro Justen <https://github.com/turicas/rows/>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

from collections import OrderedDict
from collections import namedtuple
from io import BytesIO
from urllib import quote as url_quote
from urlparse import urljoin as url_join

import click
import requests
import rows

from lxml.html import fromstring as html_tree
from rows.plugins.html import extract_text
from rows.plugins.html import tag_to_dict


URL_ROUTER_SEARCH = 'http://dd-wrt.com/routerdb/de/routerResult.php'
FIELD_NAMES = ['id', 'manufacturer', 'model', 'revision', 'supported',
               'activation_required']
Router = namedtuple('Router', ('model', 'chipset', 'ram', 'flash', 'images'))


def _router_detail(router_id):
    response = requests.post(URL_ROUTER_SEARCH,
                             data={'action': 'routerDetail',
                                   'id': router_id,
                                   'site': 'drupal', })
    return response.content


def router_specs(router_id):
    html = _router_detail(router_id)
    tree = html_tree(html)

    model = tree.xpath('//div/h1/descendant::text()')[0]
    chipset, ram, flash = \
            tree.xpath('//div/table/tr[@class="info"]/td[1]/text()')[:3]

    table = rows.Table(fields=OrderedDict([('model', rows.fields.TextField),
                                           ('chipset', rows.fields.TextField),
                                           ('ram', rows.fields.TextField),
                                           ('flash', rows.fields.TextField)]))
    table.append({'model': model,
                  'chipset': chipset,
                  'ram': ram,
                  'flash': flash, })
    return table


def router_images(router_id):
    html = _router_detail(router_id)
    table = rows.import_from_html(BytesIO(html), index=1, preserve_html=True)
    fields = OrderedDict([('date', rows.fields.DateField),
                          ('filename', rows.fields.TextField),
                          ('url', rows.fields.TextField),
                          ('size', rows.fields.TextField),
                          ('description', rows.fields.TextField)])

    def transform(row, table):
        file_data = tag_to_dict(row.filename)
        absolute_url = url_join(URL_ROUTER_SEARCH,
                                url_quote(file_data['href']))
        return {'date': extract_text(row.date),
                'description': extract_text(row.description),
                'filename': file_data['text'],
                'size': extract_text(row.size),
                'url': absolute_url, }

    return rows.transform(fields, transform, table)


def transform_row(row, table):
    data = row._asdict()
    properties = data['properties']
    del data['properties']
    data['id'] = int(properties['onclick'].split("'")[1])
    return data


def search_router_database(query):
    response = requests.post(URL_ROUTER_SEARCH,
                             data={'action': 'routerList',
                                   'criteria': query,
                                   'site': 'drupal', })
    table = rows.import_from_html(BytesIO(response.content),
                                  encoding=response.encoding,
                                  properties=True)

    fields = OrderedDict()
    fields['id'] = rows.fields.IntegerField
    for field_name in FIELD_NAMES:
        if field_name in table.fields:
            fields[field_name] = table.fields[field_name]

    return rows.transform(fields, transform_row, table)


def filter_row(row, kwargs):
    for key, value in kwargs.items():
        if getattr(row, key) != value:
            break
    else:
        return True
    return False


def query_table(table, *args, **kwargs):
    new_table = rows.Table(fields=table.fields)
    new_table.extend(row._asdict() for row in table if filter_row(row, kwargs))
    return new_table


@click.group()
def cli():
    pass


def _create_response(result, output):
    if not output:
        rows.export_to_txt(result, sys.stdout)
    else:
        rows.utils.export_to_uri(output, result)


@cli.command(help='Search dd-wrt router database')
@click.option('--output', help='Output file to save result (CSV, HTML etc.)')
@click.option('--all',
              is_flag=True,
              default=False,
              help='Show all routers (even not supported by dd-wrt)')
@click.argument('query')
def search(query, output, all):
    result = search_router_database(query)
    result.order_by('manufacturer')
    if not all:
        result = query_table(result, supported='yes')

    _create_response(result, output)


@cli.command(help='Retrieve router specs')
@click.argument('router_id')
@click.option('--output', help='Output file to save result (CSV, HTML etc.)')
def specs(router_id, output):
    result = router_specs(router_id)
    _create_response(result, output)


@cli.command(help='Retrieve router download images')
@click.argument('router_id')
@click.option('--output', help='Output file to save result (CSV, HTML etc.)')
def images(router_id, output):
    result = router_images(router_id)
    _create_response(result, output)


if __name__ == '__main__':
    cli()
