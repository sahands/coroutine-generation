def postorder(tree):
    if not tree:
        return
    yield from postorder(tree['left'])
    yield from postorder(tree['right'])
    yield tree['value']
