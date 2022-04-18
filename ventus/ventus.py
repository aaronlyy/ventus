# ventus.py

import requests
from bs4 import BeautifulSoup

class Filter:
    """google dork filters
    """
    ALLINTEXT = "allintext:" # Searches for occurrences of all the keywords given.
    INTEXT = "intext:" # Searches for the occurrences of keywords all at once or one at a time.
    INURL = "inurl:" # Searches for a URL matching one of the keywords.
    ALLINURL = "allinurl:" # Searches for a URL matching all the keywords in the query.
    INTITLE = "intitle:" # Searches for occurrences of keywords in title all or one.
    ALLINTITLE = "allintitle:" # Searches for occurrences of keywords all at a time.
    SITE = "site:" # Specifically searches that particular site and lists all the results for that site.
    FILETYPE = "filetype:" # Searches for a particular filetype mentioned in the query.
    LINK = "link:" # Searches for external links to pages.
    NUMRANGE = "numrange:" # Used to locate specific numbers in your searches.
    BEFORE = "before:" # Used to search before a particular date.
    AFTER = "after:" # Used to search before a particular date.
    ALLINANCHOR = "allinanchor:" # This shows sites which have the keyterms in links pointing to them, in order of the most links.
    INANCHOR = "inanchor:" # This shows sites which have the keyterms in links pointing to them, in order of the most links.
    ALLINPOSTAUTHOR = "allinpostauthor:" # Exclusive to blog search, this one picks out blog posts that are written by specific individuals.
    INPOSTAUTHOR = "inpostauthor:" # Exclusive to blog search, this one picks out blog posts that are written by specific individuals.
    RELATED = "related:" # List web pages that are “similar” to a specified web page.
    CACHE = "cache:" # Shows the version of the web page that Google has in its cache.
    AND = "&"
    OR = "|"

class Engine:
    GOOGLECOM = "https://google.com/search"
    GOOGLEDE = "https://google.de/search"
    GOOGLEFR = "https://google.fr/search"
    GOOGLEES = "https://google.es/search"

class Query:
    """Build dork query
    """
    def __init__(self) -> None:
        self._query = ""
        self._query_size = 0

    def add_filter(self, filter: str, keyword: str = "", hide=False) -> None:
        """Add a filter to the query

        Args:
            filter (str | Filter): custom filter or Filter.member
            keyword (str | int): Keyword for given filter
            hide (bool): hide matches. Defaults to False.
        """
        if self._query_size > 0:
            self._query += " "
        if hide:
            self._query += "-"

        self._query += f"{filter}{keyword}"
        self._query_size += 1

    def add_keyword(self, keyword: str, hide=False) -> None:
        """Add a single keyword without a filter

        Args:
            keyword (str)
            hide (bool, optional): hide matches. Defaults to False.
        """
        if self._query_size > 0:
            self._query += " "
        if hide:
            self._query += "-"
        
        self._query += keyword
        self._query_size += 1
        

    @property
    def query(self) -> str:
        return self._query

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

if __name__ == "__main__":
    q = Query()
    q.add_filter(Filter.INTEXT, "test123")
    v = Ventus()
    print(v.search(q))