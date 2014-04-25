def multiradix(M, n, a, i):
    if i < 0:
        yield a
    else:
        for __ in multiradix(M, n, a, i - 1):
            # Extend each multi-radix number of length i with all possible
            # 0 <= x < M[i] to get a multi-radix number of length i + 1.
            for x in range(M[i]):
                a[i] = x
                yield a


def multiradix_recursive(M):
    n = len(M)
    a = [0] * n
    return multiradix(M, n, a, n - 1)
