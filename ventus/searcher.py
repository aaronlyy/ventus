import requests
from bs4 import BeautifulSoup

from .query import Query

class Searcher:
    def __init__(self):
        """
        Args:
            engine (str): query url from a searchengine (ex. Engine.GOOGLECOM)
        """
        self._engine = "https://google.com/search"

    def _request(self, query: str) -> str:
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        res = requests.get(self._engine,
        headers=headers,
        params=dict(q=query)
        )
        res.raise_for_status()
        return res.text

    def _parse(self, html: str) -> list:
        soup = BeautifulSoup(html, "html.parser")
        blocks = soup.find_all("div", attrs={"class": "g"})
        links = []
        for result in blocks:
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
        if type(query) == Query:
            query_string = query.query
        else:
            query_string = query
        
        html = self._request(query_string)
        links = self._parse(html)
        return links
    
def search(query: Query) -> list:
    """Wrapper around searcher.search"""
    s = Searcher()
    return s.search(query)
