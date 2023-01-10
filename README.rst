# Wall Check command line interface tool v0.1.0
## Overview
This tool is used for performing a mall wall check from the the backend.

The repository of this tool can be found [here](https://github.com/mihamieat/wall-check-cli).
## Pre-requisites
### Requirement
Python 3.7 and above.
### Install
We recommende you to use a virtual environment before intalling and lauching the scripts.
e.g. Virtualenv.

Then you can install the tool by doing:

    pip install git+https://github.com/mihamieat/wall-check-cli.git

## Run the application

    walls-check-cli --h
        Usage: walls-check-cli [OPTIONS]
    
      This is the tool for interacting with the wall checking endpoint.
    
    Options:
      -m, --mall INTEGER  [required]
      --url TEXT          URL of the backend's API  [required]
      --user TEXT         [required]
      --password TEXT     [required]
      --help              Show this message and exit.

Following options can be set as environment variables:

|  *option* | *environment variable*  |
|---|---|
| --url  | WC_URL  |
| --user  | WC_USER  |
| --password | WC_PASSWORD  |

## Contribute

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
