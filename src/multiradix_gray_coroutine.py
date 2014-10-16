from nobody import nobody
from stich import stitch


def local(M, a, i):
    d = +1
    while True:
        a[i] += d
        if (d == 1 and a[i] < M[i]) or (d == -1 and a[i] >= 0):
            yield True
        else:
            a[i] -= d
            d = -d
            yield False


def setup(M):
    n = len(M)
    a = [0] * n
    lead = nobody()
    for i in range(n):
        lead = stitch(local(M, a, n - i - 1), lead)
    return a, lead


def multiradix_gray_coroutine(M):
    a, lead = setup(M)
    yield a
    while next(lead):
        yield a
