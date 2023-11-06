def open(expander, node):
    node.check = expander.env.find(node.attrs["z-if"])
    if node.check:
        expander.showTag(node, False)
    return node.check

def close(expander, node):
    if node.check:
        expander.showTag(node, True)
