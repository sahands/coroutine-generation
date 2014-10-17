from nobody import nobody


def troll(a, i):
    previous = troll(a, i - 1) if i > 0 else nobody()
    while True:
        a[i] = 1 - a[i]
        yield True
        yield next(previous)


def setup(n):
    a = [0] * n
    lead_coroutine = troll(a, n - 1)
    return a, lead_coroutine


def gray(n):
    a, lead = setup(n)
    yield a
    while next(lead):
        yield a
