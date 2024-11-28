# Python entry point utility

Simple utility for grabbing Python entry points from environment by group, name and / or value.

## Usage

Currently supports Python 3.9's `importlib.metadata` API.

Get entry points with names `invenio_ldapclient` and `invenio_accounts_ui` from entry point group `invenio_base.apps`

```
from entry_point_util import entry_point_getter as epg
eps = epg(("invenio_ldapclient", None, "invenio_base.apps")) | \
      epg(("invenio_accounts_ui", None, "invenio_base.apps"))      
```

## Development

### Install

```
git clone entry-point-util
cd entry-point-util
python -m venv .venv
. .venv/bin/activate
pip install --upgrade pip && pip install '.[dev]'
```
### Build the docs

```
. .venv/bin/activate
cd docs
make html
firefox build/html/index.html
```

### Run the tests

`cd` to project root directory and run pytest

```
cd entry-point-util
pytest
```
