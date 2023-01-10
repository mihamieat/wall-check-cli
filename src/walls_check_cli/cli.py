"""Command line interface entry point."""
import click
import requests


@click.command
@click.option("-m", "--mall", required=True, type=int)
@click.option("--url", required=True, envvar="URL", type=str, help="URL of the backend's API")
@click.option("--user", required=True, type=str)
@click.option("--password", required=True, type=str)
def cli(mall, url, user, password):
    """This is the tool for interacting with the wall checking endpoint."""
    pass


if __name__ == "__main__":
    cli()
