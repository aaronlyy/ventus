# ventus.py
import urllib.parse
import requests

from query import Query
from filter import Filter
from engine import Engine


class Ventus:
    def __init__(self, engine: str):
        """
        Args:
            engine (str): query url from a searchengine (ex. Engine.GOOGLECOM)
        """
        self._engine = engine

    def _build_url(self, query: Query) -> str:
        return f"{self._engine}{urllib.parse.quote(query.query)}"

    def search(self, query: str) -> list:
        """Start a dork search with given engine and query

        Args:
            
            query (str): dork query

        Returns:
            list: list of results
        """
        pass


if __name__ == "__main__":
    ventus = Ventus(Engine.GOOGLECOM)

    query = Query()
    query.add_keyword("db_password")
    query.add_filter(Filter.FILETYPE, "env")

    results = ventus.search(query)