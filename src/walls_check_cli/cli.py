"""Command line interface entry point."""
import click
import requests

from .connect import get_token


@click.command
@click.option("-m", "--mall", required=True, type=int)
@click.option(
    "--url", required=True, envvar="WC_URL", type=str, help="URL of the backend's API"
)
@click.option("--user", required=True, envvar="WC_USER", type=str)
@click.option("--password", required=True, envvar="WC_PASSWORD", type=str)
def cli(mall, url, user, password):
    """This is the tool for interacting with the wall checking endpoint."""
    token = get_token(url, user, password)
    return token


if __name__ == "__main__":
    cli()
