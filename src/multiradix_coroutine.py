from nobody import nobody
from stich import stitch


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
    lead = nobody()
    for i in range(n):
        lead = stitch(local(M, a, n - i - 1), lead)
    return a, lead


def multiradix_coroutine(M):
    a, lead = setup(M)
    yield a
    while next(lead):
        yield a
