from nobody import nobody


def troll(n, k, a, coroutines):
    next_up = coroutines[k + 1] if k + 1 < n else nobody()
    next_down = coroutines[k + 2] if k + 2 < n else nobody()

    if a[k] == 1 or k % 2 == 1:
        next_up, next_down = next_down, next_up

    while True:
        while next(next_up):
            yield True
        a[k] = 1 - a[k]
        yield True

        while next(next_down):
            yield True
        yield False

        next_up, next_down = next_down, next_up


def setup(n):
    # Initialize a to be the first n bits
    # in 000111000111000111...
    a = [0, 0, 0, 1, 1, 1] * (n // 6 + 1)
    a = a[:n]
    coroutines = []
    coroutines.extend(troll(n, k, a, coroutines)
                      for k in range(n))
    coroutines[0]
    return a, coroutines[0]
