from nobody import nobody
from stitch_coroutines import stitch_coroutines


def local(M, a, i):
    while True:
        if a[i] == M[i] - 1:
            a[i] = 0
            yield False
        a[i] += 1
        yield True


def setup(M):
    n = len(M)
    a = [0] * n
    coroutines = [local(M, a, i) for i in range(n)] + [nobody()]
    lead = stitch_coroutines(coroutines)
    return a, lead


def multiradix_coroutine(M):
    a, lead = setup(M)
    yield a
    while next(lead):
        yield a
