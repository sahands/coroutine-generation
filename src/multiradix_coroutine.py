from nobody import nobody


def local(M, a, i):
    while True:
        if a[i] == M[i] - 1:
            a[i] = 0
            yield False
        a[i] += 1
        yield True


def glue(X, Y):
    while True:
        while next(Y):
            yield True
        yield next(X)


def setup(M):
    n = len(M)
    a = [0] * n
    head = nobody()
    for i in range(n):
        head = glue(local(M, a, n - i - 1), head)
    return a, head


def multiradix_coroutine(M):
    a, lead = setup(M)
    yield a
    while next(lead):
        yield a
