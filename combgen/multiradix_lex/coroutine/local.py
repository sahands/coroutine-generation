def local(M, a, i):
    while True:
        a[i] = (a[i] + 1) % M[i]
        yield a[i] != 0
