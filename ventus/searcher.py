# searcher.py
import requests
from bs4 import BeautifulSoup
from query import Query

class Searcher:
    def __init__(self, engine):
        self._engine = engine
    
    def _request(self, query: Query) -> requests.Response:
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        res = requests.get(self._engine,
        headers=headers,
        params=dict(q=query.query)
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
        html = self._request(query)
        links = self._parse(html)
        return links


