# filter.py

class Filter:
    """List of google dork filters
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