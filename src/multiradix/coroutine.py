from nobody import nobody


def local(M, a, i):
    while True:
        if a[i] == M[i] - 1:
            yield False
            a[0] = 0


def glue(M, a, i):

def troll(M, a, i):
    previous = troll(M, a, i - 1) if i > 0 else nobody()
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
    lead = troll(M, a, n - 1)
    yield a
    while next(lead):
        yield a
