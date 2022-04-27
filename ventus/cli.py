# cli.py

import click

from .wrapper import search as v_search
from .wrapper import search_onlyfans as v_onlyfans
from .wrapper import search_index_of as v_index

LINKVERTISE_MESSAGE = "---\n!!! Redirected to linkvertise.com? Use 'thebypasser.com' to bypass linkvertise links! !!!\n---"

@click.group()
def cli():
    pass

@cli.command()
@click.argument("query")
def search(query: str) -> None:
    """Search a query on Google

    Args:
        query (str): Query
    """
    results = v_search(query)
    if len(results) > 0:
        for url in results:
            print(url)
    click.echo(LINKVERTISE_MESSAGE)

@cli.command()
@click.argument("name")
def onlyfans(name: str) -> None:
    """Find leaks of onlyfans models

    Args:
        query (str): Query
    """
    results = v_onlyfans(name)
    if len(results) > 0:
        for url in results:
            print(url)
    click.echo(LINKVERTISE_MESSAGE)

@cli.command()
@click.argument("folder")
def indexof(folder: str) -> None:
    """Predefined 'index of /' search

    Args:
        folder (str): Name of folder
    """
    results = v_index(folder)
    if len(results) > 0:
        for url in results:
            print(url)
    click.echo(LINKVERTISE_MESSAGE)

if __name__ == "__main__":
    cli()