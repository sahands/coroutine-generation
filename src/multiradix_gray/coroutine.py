from itertools import cycle


def nobody():
    while True:
        yield False


def reflected_cycle(n):
    """Cycle through 0, 1, ..., n-1, n - 1, n - 2, ..., 1, 0"""
    return cycle(list(range(n)) + list(range(n - 1, 0, -1)))


def troll(M, a, i):
    d = 1
    neighbour = troll(M, a, i + 1) if i < len(M) - 1 else nobody()
    while True:
        while next(neighbour):
            yield True
        a[i] += d
        if (d == 1 and a[i] < M[i]) or (d == -1 and a[i] >= 0):
            yield True
        else:
            a[i] -= d
            d = -d
            yield False


def multiradix_coroutine(M):
    n = len(M)
    a = [0] * n
    lead = troll(M, a, 0)
    yield a
    while next(lead):
        yield a


def main():
    c = 0
    for p in multiradix_coroutine([2, 3, 3]):
        c += 1
        print(''.join(str(x) for x in p))
    print(c)


if __name__ == '__main__':
    main()
