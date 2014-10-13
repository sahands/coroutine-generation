from nobody import nobody


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


def glue(X, Y):
    while True:
        while next(Y):
            yield True
        yield next(X)


def setup(M):
    n = len(M)
    a = [0] * n
    lead = nobody()
    for i in range(n):
        lead = glue(local(M, a, n - i - 1), lead)
    return a, lead


def multiradix_gray_coroutine(M):
    a, lead = setup(M)
    yield a
    while next(lead):
        yield a
