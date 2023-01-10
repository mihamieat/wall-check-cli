"""Command line interface entry point."""
import click
import requests


@click.command
@click.option("-m", "--mall", required=True, type=int)
@click.option("--url", required=True, envvar="URL",type=str)
def cli(mall, url):
    """This is the tool for interacting with the wall checking endpoint."""
    pass

if  __name__  ==  '__main__':
	cli()