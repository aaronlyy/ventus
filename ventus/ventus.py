# ventus.py
from query import Query
from engine import Engine
from searcher import Searcher

class Ventus:
    def __init__(self, engine: str = Engine.GOOGLECOM):
        """
        Args:
            engine (str): query url from a searchengine (ex. Engine.GOOGLECOM)
        """
        self._searcher = Searcher(engine)

    def search(self, query: Query) -> list:
        """Start a dork search with given query

        Args:
            
            query (str): dork query

        Returns:
            list: list of results
        """
        links = self._searcher.search(query)
        return links