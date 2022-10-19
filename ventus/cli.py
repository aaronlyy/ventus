# cli.py

import click

from .wrapper import search as wrapper_search
from .wrapper import leak as wrapper_leak
from .wrapper import index_of as wrapper_index
from .wrapper import presentation as wrapper_presentation
from .wrapper import document as wrapper_document

LINKVERTISE_MESSAGE = "---\n!!! Redirected to linkvertise.com? Use 'thebypasser.com' to bypass linkvertise links! !!!\n---"

@click.command()
@click.option("-l", "--leak", default=False, required=False, is_flag=True)
@click.option("-p", "--presentation", default=False, required=False, is_flag=True)
@click.option("-i", "--index", default=False, required=False, is_flag=True)
@click.option("-d", "--document", default=False, required=False, is_flag=True)
@click.argument("query")
def cli(leak, presentation, document, index, query) -> None:
    if (leak):
        click.echo(LINKVERTISE_MESSAGE)
        results = wrapper_leak(query)
    elif (index):
        results = wrapper_index(query)
    elif (document):
        results = wrapper_document(query)
    elif (presentation):
        results = wrapper_presentation(query)
    else:
        results = wrapper_search(query)
    
    if (len(results) > 0):
        for url in results:
            click.echo(f"[+] {url}")
    else:
        click.echo("No results. Try a different method/query or use a VPN.")
if __name__ == "__main__":
    cli()