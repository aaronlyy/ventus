from .searcher import Searcher
from .query import Query
from .sites import Site
from .extension import Extension

def search(query: Query) -> list:
    """Wrapper around searcher.search"""
    s = Searcher()
    return s.search(query)

def index_of(folder: str) -> list:
    """Search exposed folders"""
    q = Query()
    q.allintitle(f"index of /{folder}")
    results = []
    for r in search(q):
        results.append(r)
    return results

def leak(query: str) -> list:
    """Search leaks"""
    results = []
    for s in Site.LIST_LEAK:
        q = Query()
        q.raw(query)
        q.site(s)
        print(q)
        r = search(q)
        results.extend(r)
    for s in Site.LIST_PASTING:
        q = Query()
        q.raw(query)
        q.site(s)
        print(q)
        r = search(q)
        results.extend(r)
    for s in Site.LIST_FILESHARING:
        q = Query()
        q.raw(query)
        q.site(s)
        print(q)
        r = search(q)
        results.extend(r)
    return results

def presentation(query: str) -> list:
    results = []
    q = Query()
    q.intitle(query)
    q.filetype([Extension.PPTX, Extension.PDF])
    r = search(q)
    results.extend(r)
    return results

def document(query: str) -> list:
    results = []
    q = Query()
    q.intitle(query)
    q.filetype([Extension.PDF, Extension.DOCX])
    r = search(q)
    results.extend(r)
    return results