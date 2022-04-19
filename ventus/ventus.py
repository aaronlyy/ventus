# ventus.py
from unittest import result
import requests
from bs4 import BeautifulSoup

class Filter:
    """Dork filters"""
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
    EXT = "ext:" # Searches for a particular filetype mentioned in the query.
    AND = "&"
    OR = "|"
    AND2 = "AND"
    OR2 = "OR"

class Ext:
    # predefined filetypes for fast use
    PDF = "pdf"
    # word
    DOC = "doc"
    DOT = "dot"
    WBK = "wbk"
    DOCX = "docx"
    DOTX = "dotx"
    DOTM = "dotm"
    DOCB = "docb"
    WLL = "wll"
    WWL = "wwl"
    # excel
    XLS = "xls"
    XLT = "xlt"
    XLM = "xlm"
    XLL_ = "xll_"
    XLA_ = "xla_"
    XLA5 = "xla5"
    XLA8 = "xla8"
    XLSX = "xlsx"
    XLSM = "xlsm"
    XLTS = "xltx"
    XLTM = "xltm"
    XLSB = "xlsb"
    XLA = "xla"
    XLAM = "xlam"
    XLL = "xll"
    XLW = "xlw"
    # powepoint
    PPT = "ppt"
    POT = "pot"
    PPS = "pps"
    PPA = "ppa"
    PPAM = "ppam"
    PPTX = "pptx"
    PPTM = "pptm"
    POTX = "potx"
    POTM = "potm"
    PPAM = "ppam"
    PPSX = "ppsx"
    PPSM = "ppsm"
    SLDX = "sldx"
    SLDM = "sldm"
    PA = "pa"
    # videos
    MOV = "mov"
    MP4 = "mp4"
    WMV = "wmv"
    AVI = "avi"
    AVCHD = "avchd"
    FLV = "flv"
    F4V = "f4v"
    SWF = "swf"
    MKV = "mkv"
    WEBM = "webm"
    OGG = "ogg"
    OGV = "ogv"
    MPG = "mpg"
    AAC = "aac"
    WMA = "wma"
    # images
    JPG = "jpg"
    JPEG = "jpeg"
    JIFF = "jiff"
    PJPEG = "pjpeg"
    PJP = "pjp"
    PNG = "png"
    SVG = "svg"
    WEBP = "webp"
    GIF = "gif"
    BMP = "bmp"
    ICO = "ico"
    CUR = "cur"
    TIF = "tif"
    TIFF = "tiff"
    AVIF = "avif"
    APNG = "apng"
    # lists
    LIST_IMAGE = [JPG, JPEG, JIFF, PJPEG, PJP, PNG, SVG, WEBP, GIF, BMP, ICO, CUR, TIF, TIFF, AVIF, APNG]
    LIST_VIDEO = [MOV, MP4, WMV, AVI, AVCHD, FLV, F4V, SWF, MKV, WEBM, OGG, OGV, MPG, AAC, WMA]
    LIST_POWERPOINT = [PPT, POT, PPS, PPA, PPAM, PPTX, PPTM, POTX, POTM, PPAM, PPSX, PPSM, SLDX, SLDM, PA]
    LIST_EXCEL = [XLS, XLT, XLM, XLL_, XLA_, XLA5, XLA8, XLSX, XLSM, XLTS, XLSB, XLA, XLAM, XLL, XLW]
    LIST_WORD = [DOC, DOT, WBK, DOCX, DOTX, DOTM, DOCB, WLL, WWL]

class Sites:
    """Collection of some useful sites for dorking"""
    # file sharing
    GOOGLEDRIVE = "drive.google.com"
    GOFILE = "gofile.io"
    ANONFILE = "anonfile.com"
    BAYFILES = "bayfiles.com"
    # pasting
    JUSTPASTE = "justpaste.it"
    FAMOUSPASTE = "famouspaste.com"
    PASTELINK = "pastelink.net"
    NULLBIN = "0bin.net"
    RENTRY = "rentry.co"
    PASTESITE = "pastesite.org"
    FREEPASTE = "freepaste.link"
    LEAKLINKS = "leaklinks.com"
    JUSTPASTE = "justpaste.it"
    PASTEBIN = "pastebin.com"
    # lists
    LIST_FILESHARING = [GOOGLEDRIVE, GOFILE, ANONFILE, BAYFILES]
    LIST_PASTING = [JUSTPASTE, FAMOUSPASTE, PASTELINK, NULLBIN, RENTRY, PASTESITE, FREEPASTE, LEAKLINKS, JUSTPASTE, PASTEBIN]

class Indexing:
    CRACKS = "cracks"
    CRACK = "crack"
    LEAK = "leak"
    LEAKS = "leaks"
    LASTMOD = "lastmodified"
    LIST_CRACK = [CRACKS, LEAKS, CRACK, LEAK]

class Engine:
    """Searchengine URL's"""
    GOOGLECOM = "https://google.com/search"
    GOOGLEDE = "https://google.de/search"
    GOOGLEFR = "https://google.fr/search"
    GOOGLEES = "https://google.es/search"

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

    def _build_subquery_string(self, filter: str, keywords: str | list, group_seperator: str, hide: bool = False) -> str:
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

    def allintext(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for occurrences of all the keywords given."""
        sub = self._build_subquery_string(Filter.ALLINTEXT, keywords, group_seperator, hide)
        self._append_query_string(sub)
    
    def intext(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for the occurrences of keywords all at once or one at a time."""
        sub = self._build_subquery_string(Filter.INTEXT, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def inurl(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for a URL matching one of the keywords."""
        sub = self._build_subquery_string(Filter.INURL, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def allinurl(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for a URL matching all the keywords."""
        sub = self._build_subquery_string(Filter.ALLINURL, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def intitle(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for occurrences of keywords in title all or one."""
        sub = self._build_subquery_string(Filter.INTITLE, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def allintitle(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for occurrences of keywords in the title all at a time."""
        sub = self._build_subquery_string(Filter.ALLINTITLE, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def site(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Specifically searches that particular site and lists all the results for that site."""
        sub = self._build_subquery_string(Filter.SITE, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def filetype(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for a particular filetype mentioned in the query."""
        sub = self._build_subquery_string(Filter.FILETYPE, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def link(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for external links to pages."""
        sub = self._build_subquery_string(Filter.LINK, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def numrange(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Used to locate specific numbers in your searches."""
        sub = self._build_subquery_string(Filter.NUMRANGE, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def before(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Used to search before a particular date."""
        sub = self._build_subquery_string(Filter.BEFORE, keywords, group_seperator, hide)
        self._append_query_string(sub)
    
    def after(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Used to search before a particular date."""
        sub = self._build_subquery_string(Filter.AFTER, keywords, group_seperator, hide)
        self._append_query_string(sub)
    
    def allinanchor(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """This shows sites which have the keyterms in links pointing to them, in order of the most links."""
        sub = self._build_subquery_string(Filter.ALLINANCHOR, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def inanchor(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """This shows sites which have the keyterms in links pointing to them, in order of the most links."""
        sub = self._build_subquery_string(Filter.INANCHOR, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def allinpostauthor(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Exclusive to blog search, this one picks out blog posts that are written by specific individuals."""
        sub = self._build_subquery_string(Filter.ALLINPOSTAUTHOR, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def inpostauthor(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Exclusive to blog search, this one picks out blog posts that are written by specific individuals."""
        sub = self._build_subquery_string(Filter.INPOSTAUTHOR, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def related(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """List web pages that are “similar” to a specified web page."""
        sub = self._build_subquery_string(Filter.RELATED, keywords, group_seperator, hide)
        self._append_query_string(sub)
    
    def cache(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Shows the version of the web page that Google has in its cache."""
        sub = self._build_subquery_string(Filter.CACHE, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def ext(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Searches for a particular filetype mentioned in the query."""
        sub = self._build_subquery_string(Filter.EXT, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def symbol_and(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Adds a & symbol."""
        sub = self._build_subquery_string(Filter.AND, keywords, group_seperator, hide)
        self._append_query_string(sub)
    
    def written_and(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Adds an AND."""
        sub = self._build_subquery_string(Filter.AND2, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def symbol_or(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
        """Adds a | symbol."""
        sub = self._build_subquery_string(Filter.OR, keywords, group_seperator, hide)
        self._append_query_string(sub)

    def written_or(self, keywords: str | list, hide: bool = False, group_seperator: str = "|") -> None:
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

class Searcher:
    def __init__(self, engine: str = Engine.GOOGLECOM):
        """
        Args:
            engine (str): query url from a searchengine (ex. Engine.GOOGLECOM)
        """
        self._engine = engine

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

    def search(self, query: Query | str) -> list:
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

def search(query: Query | str) -> list:
    """Wrapper around ventus.search"""
    s = Searcher()
    return s.search(query)

# predefined searches
def search_index_of(folder: str) -> list:
    q = Query()
    q.allintitle(f"index of /{folder}")
    results = []
    for r in search(q):
        results.append(r)
    return results

def search_onlyfans(name: str) -> list:
    results = []
    for s in Sites.LIST_PASTING:
        q = Query()
        q.raw(name)
        q.site(s)
        r = search(q)
        results.extend(r)
    return results