# Alloff Backoffice Server

- [Alloff Backoffice Server](#alloff-backoffice-server)
  - [Installation](#installation)
    - [Before we begin...](#before-we-begin)
    - [Requirements](#requirements)
    - [Install dependencies](#install-dependencies)
  - [Run server](#run-server)

## Installation

### Before we begin...
If you're developing on Apple silicons, and you encounter some error like the following ---
`Error occurred during checks: ImportError("dlopen(/Users/some-user/Library/Caches/pypoetry/virtualenvs/alloff-backoffice-server-5VJGsauF-py3.10/lib/python3.10/site-packages/grpc/_cython/cygrpc.cpython-310-darwin.so, 0x0002): tried: '/Users/some-user/Library/Caches/pypoetry/virtualenvs/alloff-backoffice-server-5VJGsauF-py3.10/lib/python3.10/site-packages/grpc/_cython/cygrpc.cpython-310-darwin.so' (mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64e')), '/usr/lib/cygrpc.cpython-310-darwin.so' (no such file)")`, 

try installing grpcio-tools with the following command:
```bash
pip3 install --no-binary :all: grpcio-tools --ignore-installed
```

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