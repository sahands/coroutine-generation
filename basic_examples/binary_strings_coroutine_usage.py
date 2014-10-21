from time import sleep
from binary_strings_coroutine import troll


def setup(n):
    a = [0] * n
    lead = troll(n, a, neighbour=None)  # Start with the last troll in line
    for i in range(n):
        lead = troll(n, a, i, neighbour=lead)
    return a, lead


def visit(a):
    print(''.join(str(x) for x in a))


def print_binary_strings_in_lex(n):
    a, lead = setup(n)
    while True:
        visit(a)
        if not next(lead):
            print('---')  # Alternatively, break
            sleep(1)

print_binary_strings_in_lex(3)
