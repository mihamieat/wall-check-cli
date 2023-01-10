===============
Wall Check command line interface tool v0.1.0
===============

---------------
Overview
---------------

This tool is used for performing a mall wall check from the the backend.

The repository of this tool can be found `here`_.

.. _here: https://github.com/mihamieat/wall-check-cli

---------------
Pre-requisites
---------------

Requirements
===============

Python 3.7 and above.

Install
===============

We recommend you to use a virtual environment before intalling and lauching the scripts.
e.g. virtualenv.

Then you can install the tool by doing:

..  code-block:: sh

    pip install git+https://github.com/mihamieat/wall-check-cli.git

---------------
Run the application
---------------

..  code-block:: sh

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

.. list-table::
   :widths: 25 25
   :header-rows: 1

   * - option
     - environment variable
   * - --url
     - WC_URL
   * - --user
     - WC_USER
   * - --password
     - WC_PASSWORD

---------------
Contribute
---------------

For development purposes, we use Poetry.

Poetry
===============

We recommend you to install Poetry.
Poetry is a tool for dependency management and packaging in Python.
see [Poetry docs](https://python-poetry.org/docs/).

..  code-block:: sh

    curl -sSL https://install.python-poetry.org | python3 -

Clone the project and go to the project directory.
And then install dependencies:

..  code-block:: sh

    poetry install

Run a command inside the project’s virtualenv.
===============

To run a command, in the poetry project virtualenc, do:

..  code-block:: sh

    poetry run wall-check-cli

To run shell in the virtual environment, do:

..  code-block:: sh

    poetry shell
