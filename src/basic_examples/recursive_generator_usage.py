from collections import defaultdict
from recursive_generator import postorder

# Let's build a simple tree representing (1 + 3) * (4 - 2)
tree = lambda: defaultdict(tree)
T = tree()
T['value'] = '*'
T['left']['value'] = '+'
T['left']['left']['value'] = '1'
T['left']['right']['value'] = '3'
T['right']['value'] = '-'
T['right']['left']['value'] = '4'
T['right']['right']['value'] = '2'

postfix = list(postorder(T))
print(postfix)  # ['1', '3', '+', '4', '2', '-', '*']
