

<p align="center">
  <img src=".\media\banner.png" alt="banner">
</p>

<h3 align="center">A Google Dorking library & Command-Line Interface 👾</h3>

<p align="center">
  <img alt="GitHub" src="https://img.shields.io/github/license/aaronlyy/ventus">
</p>

## Installation

Install ventus with pip

```pip install ventus```

## Usage (command-line interface)

```txt
Usage: ventus [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  indexof   Predefined 'index of /' search
  onlyfans  Find leaks of onlyfans models
  search    Search a query on Google
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

## To Do

- Add support for proxy lists
- Add more command-line interface endpoints & options
- Add option to choose number of links to return
- Write more predefined queries
- Add more Examples and Documentation

### About

Made with ♥ by [aaronlyy](https://github.com/aaronlyy)
