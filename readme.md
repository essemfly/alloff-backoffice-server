# Alloff Backoffice Server

- [Installation](#installation)
  - [Requirements](#requirements)
  - [Install dependencies](#install-dependencies)
- [Run server](#run-server)

## Installation

### Requirements

- [poetry](https://python-poetry.org/)
- python 3.9^
- env files (ask teammate!)

### Install dependencies

```bash
git clone https://github.com/lessbutter/alloff-backoffice-server.git
cd alloff-backoffice-server
poetry install
```

## Run server

```bash
poetry activate
poetry shell
# then
(some-env) $ python manage.py runserver # default port 8000
```

OR

```bash
poetry run ./manage.py runserver
# OR
poetry run ./manage.py runserver_plus # _plus supports interactive debugging
```
