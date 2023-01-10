# Wall Check command line interface tool
## Overview
This tool is used for performing a mall wall check from the the backend[here](https://www.data-transitionnumerique.com/scikit-learn-python/)
## Pre-requisites
### Requirement
Python 3.7 and above.
### Install
We recommende you to use a virtual environment before intalling and lauching the scripts.
e.g. Using Virtualenv
Then you can install the tool.

    pip install git+https://github.com/mihamieat/wall-check-cli.git

## Contrubute
For development purposes, we use Poetry.
### Poetry
We recommend you to install Poetry.
Poetry is a tool for dependency management and packaging in Python.
see [Poetry docs](https://python-poetry.org/docs/).

    curl -sSL https://install.python-poetry.org | python3 -

Clone the project and go to the project directory.
And then install dependencies:

    poetry install

### Run a script
To run a script, for instance, do:

    poetry run wall-check-cli

To run shell in the virtual environment, do:

    poetry shell
