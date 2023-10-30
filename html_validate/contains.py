import sys
from bs4 import BeautifulSoup, Tag

def recurse(node, catalog):
    assert isinstance(node, Tag)

    if node.name not in catalog:
        catalog[node.name] = set()

    for child in node:
        if isinstance(child, Tag):
            catalog[node.name].add(child.name)
            recurse(child, catalog)

    return catalog

if __name__ == "__main__":
    assert len(sys.argv) == 2, "Usage: contains.py file.html"
    data = open(sys.argv[1], "r").read()
    doc = BeautifulSoup(data, "html.parser")
    catalog = recurse(doc, {})
    print(catalog)
