# Python starter project

Python version: 3.13.3

A simple python starter project template

### Create virtual env

python -m venv .venv

Activate:

MacOS/Linux
source .venv/bin/activate

Windows:
.venv\Scripts\activate

## Install dependencies

pip install -e .
pip install pytest

## Docker support

Alternatively, you can use Docker:

docker build --target test -t myapp-test .
docker run --rm myapp-test

## Run tests

pytest

or

.venv/bin/python -m pytest

## Similar boilerplates

* at-python-template
* povanberg/python-poetry-template
* cookiecutter gh:tedivm/robs_awesome_python_template
* Python Boilerplate Templates
