def local(M, a, i):
    while True:
        if a[i] == M[i] - 1:
            a[i] = 0
            yield False
        a[i] += 1
        yield True
