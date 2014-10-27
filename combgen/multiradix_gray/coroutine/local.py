def multiradix_gray_local(M, a, i):
    while True:
        while a[i] < M[i] - 1:
            a[i] += 1
            yield True
        yield False
        while a[i] > 0:
            a[i] -= 1
            yield True
        yield False
