def postorder(tree):
    if not tree:
        return

    for x in postorder(tree['left']):
        yield x

    for x in postorder(tree['right']):
        yield x

    yield tree['value']
