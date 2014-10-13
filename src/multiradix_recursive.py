def multiradix_recursive(M, i):
    if i < 0:
        yield []
        return
    for a in multiradix_recursive(M, i - 1):
        for x in range(M[i]):
            yield a + [x]
