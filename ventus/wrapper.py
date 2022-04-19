from .searcher import Searcher
from .query import Query
from .sites import Site

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
    for s in Site.LIST_PASTING:
        q = Query()
        q.raw(name)
        q.site(s)
        r = search(q)
        results.extend(r)
    return results