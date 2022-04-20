from .searcher import Searcher
from .query import Query
from .sites import Site

def search(query: Query | str) -> list:
    """Wrapper around searcher.search"""
    s = Searcher()
    return s.search(query)

def search_index_of(folder: str) -> list:
    """Search exposed folders"""
    q = Query()
    q.allintitle(f"index of /{folder}")
    results = []
    for r in search(q):
        results.append(r)
    return results

def search_onlyfans(name: str) -> list:
    """Search leaks of OnlyFans.com users"""
    results = []
    for s in Site.LIST_PASTING:
        q = Query()
        q.raw(name)
        q.site(s)
        r = search(q)
        results.extend(r)
    return results