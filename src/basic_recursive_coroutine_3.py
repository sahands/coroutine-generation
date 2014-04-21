from collections import defaultdict


def postorder(tree):
    if not tree:
        return

    yield from postorder(tree['left'])
    yield from postorder(tree['right'])
    yield tree['value']


# Usage:
tree = lambda: defaultdict(tree)

# Let's build a simple tree representing (1 + 3) * (4 - 2)
T = tree()
T['value'] = '*'
T['left']['value'] = '+'
T['left']['left']['value'] = '1'
T['left']['right']['value'] = '3'
T['right']['value'] = '-'
T['right']['left']['value'] = '4'
T['right']['right']['value'] = '2'

# Note that since
postfix = ' '.join(str(x) for x in postorder(T))
print(postfix)  # Prints 1 3 + 4 2 - *

