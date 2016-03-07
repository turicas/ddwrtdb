# ddwrtdb

[![License: GPLv3](https://img.shields.io/pypi/l/ddwrtdb.svg)](https://github.com/turicas/ddwrtdb/blob/develop/LICENSE)
[![Current version at PyPI](https://img.shields.io/pypi/v/ddwrtdb.svg)](https://pypi.python.org/pypi/ddwrtdb)
[![Downloads per month on PyPI](https://img.shields.io/pypi/dm/ddwrtdb.svg)](https://pypi.python.org/pypi/ddwrtdb)
![Supported Python Versions](https://img.shields.io/pypi/pyversions/ddwrtdb.svg)
![Software status](https://img.shields.io/pypi/status/ddwrtdb.svg)
[![Donate](https://img.shields.io/gratipay/turicas.svg?style=social&label=Donate)](https://www.gratipay.com/turicas)


## Introduction

If you use [dd-wrt](http://dd-wrt.com/) router operating system but thinks its
router database search is boring, `ddwrtdb` is what you're looking for: it's a
simple command-line interface to query [dd-wrt's router
database](http://dd-wrt.com/site/support/router-database) -- you can also
export the result data into tabular formats such as CSV, HTML (`<table>`), XLS,
XLSX and SQLite.


## Installation

If you already have [Python pip installer](https://pypi.python.org/pypi/pip),
get it directly from [PyPI](http://pypi.python.org/pypi/ddwrtdb) by running:

    pip install ddwrtdb

If you have a strong heart, install the bleeding edge version:

    pip install git+https://github.com/turicas/ddwrtdb.git@develop

To install without pip, clone the repo and use `setup.py`:

    git clone https://github.com/turicas/ddwrtdb.git
    cd rows
    python setup.py install


> Note: if you want support for exporting XLS and XLSX files, run:

    pip install ddwrtdb[xls]
    pip install ddwrtdb[xlsx]


## Basic Usage

### Searching for Routers

Subcommand: `search`. Search into dd-wrt router database for a desired
router/manufacturer.

Syntax:

    ddwrtdb search [--all] [--output=<FILENAME>] <query>

> Note: by default will return only supported routers (use `--all` to retrieve
> even not supported routers).

Example:

    ddwrtdb search tp-link

The result will looks like this:

    +-----+--------------+---------------+--------------------+-----------+---------------------+
    |  id | manufacturer |     model     |      revision      | supported | activation_required |
    +-----+--------------+---------------+--------------------+-----------+---------------------+
    | 655 |      TP-Link |     TL-MR3020 |               v1.x |       yes |               false |
    | 656 |      TP-Link |     TL-MR3220 |               v1.x |       yes |               false |
    | 658 |      TP-Link |     TL-MR3420 |               v1.x |       yes |               false |
    | 669 |      TP-Link |    TL-WA7510N |               v1.x |       yes |               false |
    | 664 |      TP-Link |    TL-WA801ND |               v1.x |       yes |               false |
    | 532 |      TP-Link |    TL-WA901ND |               v1.x |       yes |               false |
    | 668 |      TP-Link |    TL-WA901ND |               v2.x |       yes |               false |
    | 671 |      TP-Link |    TL-WDR3600 |               v1.x |       yes |               false |
    | 672 |      TP-Link |    TL-WDR4300 |               v1.x |       yes |               false |
    | 696 |      TP-Link |    TL-WDR4310 |                1.x |       yes |               false |
    | 478 |      TP-Link | TL-WR1043N(D) |                1.x |       yes |               false |
    | 680 |      TP-Link |   TL-WR2543ND |               v1.x |       yes |               false |
    | 576 |      TP-Link |     TL-WR703N |                1.x |       yes |               false |
    | 533 |      TP-Link |     TL-WR740N |                1.x |       yes |               false |
    | 541 |      TP-Link |     TL-WR740N |                2.x |       yes |               false |
    | 697 |      TP-Link |     TL-WR740N |                3.x |       yes |               false |
    | 574 |      TP-Link |     TL-WR740N |                4.x |       yes |               false |
    | 534 |      TP-Link |    TL-WR741ND |          1.x / 2.x |       yes |               false |
    | 575 |      TP-Link |    TL-WR741ND |                4.0 |       yes |               false |
    | 673 |      TP-Link |    TL-WR743ND |               v1.x |       yes |               false |
    | 675 |      TP-Link |     TL-WR840N |               v1.x |       yes |               false |
    | 535 |      TP-Link |  TL-WR841N(D) |                3.x |       yes |               false |
    | 536 |      TP-Link |  TL-WR841N(D) |                5.x |       yes |               false |
    | 537 |      TP-Link |  TL-WR841N(D) |                7.x |       yes |               false |
    | 676 |      TP-Link |  TL-WR841N(D) |                8.x |       yes |               false |
    | 677 |      TP-Link |  TL-WR842N(D) |               v1.x |       yes |               false |
    | 678 |      TP-Link |    TL-WR940ND |               v1.x |       yes |               false |
    | 539 |      TP-Link |  TL-WR941N(D) | v1.x / v2.x / v3.x |       yes |               false |
    | 540 |      TP-Link |  TL-WR941N(D) |  v4.x / (v5.x old) |       yes |               false |
    +-----+--------------+---------------+--------------------+-----------+---------------------+


> You can export the results to a tabular file (CSV, HTML, SQLite, XLS, XLSX
> etc.) with the `--output` option as follows:

    ddwrtdb search tp-link --output=tp-link.csv


### Retrieving Router Specs

Subcommand: `specs`. Retrieve information about a router, like chipset, RAM and
Flash sizes.

Syntax:

    ddwrtdb specs [--output=<FILENAME>] <router_id>

Example:

    ddwrtdb specs 575  # cheap and cool router

The result will looks like this:

    +------------------------+---------+-------+-------+
    |         model          | chipset |  ram  | flash |
    +------------------------+---------+-------+-------+
    | TP-Link TL-WR741ND 4.0 |  AR9331 | 32 MB |  4 MB |
    +------------------------+---------+-------+-------+

> You can export the results to a tabular file (CSV, HTML, SQLite, XLS, XLSX
> etc.) with the `--output` option as follows:

    ddwrtdb search tp-link --output=tp-link.csv


### Retrieving Router Image Links

Subcommand: `images`. Retrieve image download links for a specific router.

Syntax:

    ddwrtdb images [--output=<FILENAME>] <router_id>

Example:

    ddwrtdb images 575

The result will looks like this:

    +------------+-----------------------------+------------------------------------------------------------------------------------------------+---------+--------------------------------------------------------------+
    |    date    |           filename          |                                              url                                               |   size  |                         description                          |
    +------------+-----------------------------+------------------------------------------------------------------------------------------------+---------+--------------------------------------------------------------+
    | 2013-04-25 |        factory-to-ddwrt.bin |        http://dd-wrt.com/routerdb/de/download/TP-Link/TL-WR741ND/4.0/factory-to-ddwrt.bin/4161 | 3,75 MB | WR741N v4.x Firmware - Webflash image for first installation |
    | 2013-04-24 | tl-wr741nd_v4-webrevert.rar | http://dd-wrt.com/routerdb/de/download/TP-Link/TL-WR741ND/4.0/tl-wr741nd_v4-webrevert.rar/4163 | 3,36 MB |                        WR741N v4.x Webrevert - Back to stock |
    | 2013-04-25 |   tl-wr741ndv4-webflash.bin |   http://dd-wrt.com/routerdb/de/download/TP-Link/TL-WR741ND/4.0/tl-wr741ndv4-webflash.bin/4162 | 3,75 MB |                        WR741N v4.x Firmware - Webflash image |
    +------------+-----------------------------+------------------------------------------------------------------------------------------------+---------+--------------------------------------------------------------+


> You can export the results to a tabular file (CSV, HTML, SQLite, XLS, XLSX
> etc.) with the `--output` option as follows:

    ddwrtdb search tp-link --output=tp-link.csv


## Semantic Versioning

`ddwrtdb` uses [semantic versioning](http://semver.org). Note that it means we
do not guarantee API backwards compatibility on `0.x.y` versions.


## License

This library is released under the [GNU General Public License version
3](http://www.gnu.org/licenses/gpl-3.0.html).
