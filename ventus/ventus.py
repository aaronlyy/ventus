# ventus.py

import requests
from bs4 import BeautifulSoup

from query import Query
from filter import Filter
from engine import Engine
from search import search

class Ventus:
    def __init__(self, engine: str):
        """
        Args:
            engine (str): query url from a searchengine (ex. Engine.GOOGLECOM)
        """
        self._engine = engine

    def _request(self, query):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }

        res = requests.get(self._engine, headers=headers, params=dict(q=query.query))
        res.raise_for_status()

        print(res.text)

        soup = BeautifulSoup(res.text, "html.parser")
        res_block = soup.find_all("div", attrs={"class": "g"})
        links = []
        for result in res_block:
            element = result.find("a", href=True)
            links.append(element["href"])

        return links



    def search(self, query: Query) -> list:
        """Start a dork search with given query

        Args:
            
            query (str): dork query

        Returns:
            list: list of results
        """
        links = self._request(query)
        return links


if __name__ == "__main__":
    ventus = Ventus(Engine.GOOGLECOM)

    query = Query()
    query.add_keyword("db_password")
    query.add_filter(Filter.FILETYPE, "env")

    results = ventus.search(query)

    for i in results:
        print(i)