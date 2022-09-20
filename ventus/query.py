from .filters import Filter

class Query:
    """Dork query builder"""
    def __init__(self) -> None:
        self._query = ""
        self._query_size = 0

    def _append_query_string(self, subquery: str) -> None:
        """Append given subquery to self._query (used internal, don't call)

        Args:
            subquery (str)
        """
        sub = ""
        if self._query_size > 0:
            sub += " "
        sub += subquery
        self._query += sub
        self._query_size += 1

    def _build_subquery_string(self, filter: str, keywords: list, group_seperator: str, hide: bool = False) -> str:
        sub = ""
        if hide:
            sub += "-"
        if type(keywords) == str:
            sub += f"{filter}{keywords}"
        elif type(keywords) == list:
            sub += filter
            sub += self._build_group_string(keywords, group_seperator)
        return sub

    def _build_group_string(self, keywords: list, group_seperator: str) -> str:
        return f"({f' {group_seperator} '.join(keywords)})"

    def allintext(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for occurrences of all the keywords given."""
        sub = self._build_subquery_string(Filter.ALLINTEXT, keywords, group_seperator, hide)
        self._append_query_string(sub)
    
    def intext(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for the occurrences of keywords all at once or one at a time."""
        sub = self._build_subquery_string(Filter.INTEXT, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def inurl(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for a URL matching one of the keywords."""
        sub = self._build_subquery_string(Filter.INURL, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def allinurl(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for a URL matching all the keywords."""
        sub = self._build_subquery_string(Filter.ALLINURL, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def intitle(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for occurrences of keywords in title all or one."""
        sub = self._build_subquery_string(Filter.INTITLE, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def allintitle(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for occurrences of keywords in the title all at a time."""
        sub = self._build_subquery_string(Filter.ALLINTITLE, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def site(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Specifically searches that particular site and lists all the results for that site."""
        sub = self._build_subquery_string(Filter.SITE, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def filetype(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for a particular filetype mentioned in the query."""
        sub = self._build_subquery_string(Filter.FILETYPE, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def link(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for external links to pages."""
        sub = self._build_subquery_string(Filter.LINK, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def numrange(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Used to locate specific numbers in your searches."""
        sub = self._build_subquery_string(Filter.NUMRANGE, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def before(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Used to search before a particular date."""
        sub = self._build_subquery_string(Filter.BEFORE, keywords, group_seperator, hide)
        self._append_query_string(sub)
    
    def after(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Used to search before a particular date."""
        sub = self._build_subquery_string(Filter.AFTER, keywords, group_seperator, hide)
        self._append_query_string(sub)
    
    def allinanchor(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """This shows sites which have the keyterms in links pointing to them, in order of the most links."""
        sub = self._build_subquery_string(Filter.ALLINANCHOR, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def inanchor(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """This shows sites which have the keyterms in links pointing to them, in order of the most links."""
        sub = self._build_subquery_string(Filter.INANCHOR, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def allinpostauthor(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Exclusive to blog search, this one picks out blog posts that are written by specific individuals."""
        sub = self._build_subquery_string(Filter.ALLINPOSTAUTHOR, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def inpostauthor(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Exclusive to blog search, this one picks out blog posts that are written by specific individuals."""
        sub = self._build_subquery_string(Filter.INPOSTAUTHOR, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def related(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """List web pages that are “similar” to a specified web page."""
        sub = self._build_subquery_string(Filter.RELATED, keywords, group_seperator, hide)
        self._append_query_string(sub)
    
    def cache(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Shows the version of the web page that Google has in its cache."""
        sub = self._build_subquery_string(Filter.CACHE, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def ext(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for a particular filetype mentioned in the query."""
        sub = self._build_subquery_string(Filter.EXT, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def symbol_and(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Adds a & symbol."""
        sub = self._build_subquery_string(Filter.AND, keywords, group_seperator, hide)
        self._append_query_string(sub)
    
    def written_and(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Adds an AND."""
        sub = self._build_subquery_string(Filter.AND2, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def symbol_or(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Adds a | symbol."""
        sub = self._build_subquery_string(Filter.OR, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def written_or(self, keywords: list, hide: bool = False, group_seperator: str = "|") -> None:
        """Adds an OR."""
        sub = self._build_subquery_string(Filter.OR2, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def keyword_group(self, keywords: list, group_seperator: str = "|", hide: bool = False) -> None:
        """Adds a list of keywords to the query."""
        sub = self._build_subquery_string("", keywords, group_seperator, hide)
        self._append_query_string(sub)

    def raw(self, raw: str) -> None:
        """Add a raw string to the query"""
        self._append_query_string(raw)

    @property
    def query(self) -> str:
        return self._query

    def __str__(self):
        return self.query