from binary_strings_coroutine import troll


def setup(n):
    a = [0] * n
    lead = troll(a, neighbour=None)  # Start with the last troll in line
    for i in range(n):
        lead = troll(a, i, neighbour=lead)
    return a, lead


def visit(a):
    print(''.join(str(x) for x in a))


def print_binary_strings_in_lex(n):
    a, lead = setup(n)
    while True:
        visit(a)
        if not next(lead):
            break
            # print('---')  # Alternatively, print a delimeter and keep going


print_binary_strings_in_lex(3)
