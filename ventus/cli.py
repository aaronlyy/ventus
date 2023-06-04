# cli.py

import click

from .searcher import search
from .query import Query
from .sites import Site
from .extension import Extension

BYPASS_MESSAGE = "---\nUse 'thebypasser.com' or 'bypass.pm' to bypass ad-links!\n---"

@click.command()
@click.option("-p", "--paste", default=False, required=False, is_flag=True, help="Search paste sites")
@click.option("-f", "--file", default=False, required=False, is_flag=True, help="Search filesharing sites")
@click.option("-i", "--index", default=False, required=False, is_flag=True, help="Search 'index of /<>'")
@click.option("-d", "--document", default=False, required=False, is_flag=True, help="Search for document filetypes")
@click.argument("query")
def cli(paste, file, document, index, query) -> None:
    results = []
    if (paste):
        click.echo(BYPASS_MESSAGE)
        for s in Site.LIST_PASTING:
            q = Query()
            q.raw(query)
            q.site(s)
            res = search(q)
            results.extend(res)

    elif (file):
        for s in Site.LIST_FILESHARING:
            q = Query()
            q.raw(query)
            q.site(s)
            res = search(q)
            results.extend(res)

    elif (index):
        click.echo("wip")
        q = Query()
        q.allintitle(f"index of /{query}")
        res = search(q)
        results.extend(res)

    elif (document):
        q = Query()
        q.intitle(query)
        q.filetype([Extension.PDF, Extension.DOCX])
        res = search(q)
        results.extend(res)

    else:
        results = search(query)
    
    if (len(results) > 0):
        for url in results:
            click.echo(f"[+] {url}")

    else:
        click.echo("No results. Try a different method/query or use a VPN.")

if __name__ == "__main__":
    cli()