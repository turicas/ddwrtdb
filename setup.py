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

from setuptools import setup


INSTALL_REQUIREMENTS = ['click', 'lxml', 'requests', 'rows > 0.1.1']
EXTRA_REQUIREMENTS = {
        'xls': ['xlrd', 'xlwt'],
        'xlsx': ['openpyxl'], }
EXTRA_REQUIREMENTS['all'] = sum(EXTRA_REQUIREMENTS.values(), [])
LONG_DESCRIPTION = '''
Simple CLI to search on DD-WRT router database and retrieve router information.

You can export all the results to any tabular format supported by the `rows
library <https://github.com/turicas/rows>`_ (such as CSV, XLS, XLSX, HTML an
SQLite).

To install, just run:

    pip install https://github.com/turicas/rows/archive/develop.zip
    pip install ddwrtdb

If you want support for ``XLS``, also run:

    pip install ddwrtdb[xls]

If you want support for ``XLSX``, also run:

    pip install ddwrtdb[xlsx]

The command-line interface is pretty simple to use: `read the README
<https://github.com/turicas/ddwrtdb>`_.
'''.strip()

setup(name='ddwrtdb',
      description=('Simple CLI to search on DD-WRT router database and '
                   'retrieve router information.'),
      long_description=LONG_DESCRIPTION,
      version='0.1.2',
      author=u'Álvaro Justen',
      author_email='alvarojusten@gmail.com',
      url='https://github.com/turicas/ddwrtdb/',
      py_modules=['ddwrtdb'],
      install_requires=INSTALL_REQUIREMENTS,
      extras_require=EXTRA_REQUIREMENTS,
      dependency_links=['https://github.com/turicas/rows/archive/develop.zip#egg=rows-0.2.0-dev'],
      keywords=['dd-wrt', 'router', 'database', 'tabular', 'table'],
      entry_points={
          'console_scripts': [
              'ddwrtdb = ddwrtdb:cli',
              ],
      },
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
      ]
)
