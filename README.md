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

ddwrtdb search <query>


### Retrieving Router Details


### Retrieving Router Image Links


## Semantic Versioning

`ddwrtdb` uses [semantic versioning](http://semver.org). Note that it means we
do not guarantee API backwards compatibility on `0.x.y` versions.


## License

This library is released under the [GNU General Public License version
3](http://www.gnu.org/licenses/gpl-3.0.html).
