def G():
    yield 1
    yield 2
    yield 3


def loop():
    for x in G():
        print(x)  # Prints 1, 2 and 3 on separate lines


def loop_alternative():
    g = G()
    while True:
        try:
            x = next(g)
        except StopIteration:
            break
        else:
            print(x)
