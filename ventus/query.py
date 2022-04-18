# query.py

from filter import Filter

class Query:
    def __init__(self) -> None:
        self._query = ""

    def add_filter(self, filter: str|Filter, keyword: str|int) -> None:
        self._query += f"{filter}{keyword}"

    @property
    def query(self) -> str:
        return self._query


x = Query()
x.add_filter(Filter.INTITLE, "batman")
print(x.query)