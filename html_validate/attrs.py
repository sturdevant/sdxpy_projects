from bs4 import BeautifulSoup, Tag

def display(node):
    if isinstance(node, Tag):
        print(f"node: {node.name} {node.attrs}")
        for child in node:
            display(child)

text = """<html lang="en">
<body class="outline narrow">
<p align="left" align="right">paragraph</p>
</body>
</html>"""

doc = BeautifulSoup(text, "html.parser")
display(doc)
