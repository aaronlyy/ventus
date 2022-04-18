# ventus: a google dorking library and command-line interface

## installation

install ventus with pip

```pip install ventus```

## how to use

### Example 1: Getting public database passwords

```py
from ventus import Ventus, Query, Filter

query = Query() # create a new query object
query.add_keyword("db_password") # add a single keyword
query.add_filter(Filter.FILETYPE, "env") # add a filter for filetype 'env'

ventus = Ventus() # create a ventus object
results = ventus.search(query) # execute query

for r in results:
    print(r)
```

### Example 2: Find uploaded phone backups

```py
from ventus import Ventus, Query, Filter

q = Query()
q.add_filter(Filter.INTITLE, "index of /")
q.add_filter(Filter.AND)
q.add_filter(Filter.INTEXT)
q.add_keyword_group(["Backup", "backup", "recovery"])
q.add_filter(Filter.AND)
q.add_filter(Filter.INTITLE)
q.add_keyword_group(["iphone", "samsung", "huawei"]) # default operator is Filter.OR

ventus = Ventus()
results = ventus.search(query)

for r in results:
    print(r)
```

## todo

- add support for proxy lists
- add a command-line interface wrapper
- write predefined queries

### about

made with ♥ by [aaronlyy](https://github.com/aaronlyy)
