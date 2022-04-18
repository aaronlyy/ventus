# query.py

from filter import Filter

class Query:
    """Build google dork query
    """
    def __init__(self) -> None:
        self._query = ""
        self._query_size = 0

    def add_filter(self, filter: str, keyword: str = "") -> None:
        """Add a filter to the query

        Args:
            filter (str | Filter): custom filter or Filter.member
            keyword (str | int): Keyword for given filter
        """
        if self._query_size > 0:
            self._query += " "
        
        self._query += f"{filter}{keyword}"
        self._query_size += 1

    @property
    def query(self) -> str:
        return self._query

q = Query()
q.add_filter(Filter.INTITLE, "Banane")
q.add_filter(Filter.BEFORE, "27.05.2013")
print(q.query)