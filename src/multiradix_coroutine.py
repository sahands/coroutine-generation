from nobody import nobody


def troll(M, n, a, i):
    previous = troll(M, n, a, i - 1) if i > 0 else nobody()
    while True:
        if a[i] == M[i] - 1:
            a[i] = 0
            yield next(previous)  # Poke the previous troll
        else:
            a[i] += 1
            yield True


def multiradix_coroutine(M):
    n = len(M)
    a = [0] * n
    lead = troll(M, n, a, n - 1)
    yield a
    while next(lead):
        yield a
