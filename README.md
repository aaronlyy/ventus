
<p align="center">
  <img src=".\media\banner.png" alt="banner">
</p>

<h3 align="center">A Google Dorking library & Command-Line Interface 👾</h3>

<p align="center">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/aaronlyy/ventus">
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/aaronlyy/ventus">
  <img alt="GitHub" src="https://img.shields.io/github/license/aaronlyy/ventus">
</p>

## Installation

Install ventus with pip

```pip install ventus```

## Usage (command-line interface)

```txt
Usage: ventus [OPTIONS] QUERY

Options:
  --help                Show this message and exit
  -p, --paste           Search paste sites
  -f, --files           Search filesharing sites
  -i, --index           Search index of /
  -d, --document        Search for DOCX files
```

## Usage (library)

### Example 1: Search a string

```py
from ventus import search

results = search("test")

for r in results:
    print(r)
```

### Example 2: Search a raw dork query

```py
from ventus import search

results = search("site:wikipedia.com mercedes")

for r in results:
    print(r)

for r in results:
    print(r)
```

### Example 3: Build and search a query using the query builder

```py
from ventus import search, Query

q = Query()
q.site("finance.yahoo.com")
q.intitle("AMD")

print(q) # site:finance.yahoo.com intitle:AMD

# search query
results = search(q)

for r in results:
    print(r)
```

### Example 4: Add a keyword group to a query

```py
from ventus import search, Query, Filter

q = Query()
q.site("finance.yahoo.com")
q.intitle(["BMW", "Mercedes"], group_seperator=Filter.AND)

print(q) # site:finance.yahoo.com intitle:(BMW & Mercedes)

# search query
results = search(q)

for r in results:
    print(r)
```

## Roadmap

- recode searcher and add support for pagination
- add option to choose number of links to return
- more pre configured searches in cli
- recode query builder
- show live updates while searching
- add proxy from file support
- add exceptions
- refactor all files

### About

Made with ♥ by [aaronlyy](https://github.com/aaronlyy)
