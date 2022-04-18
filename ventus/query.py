# query.py

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