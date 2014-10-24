def multiradix_gray_local(M, a, i):
    d = +1
    while True:
        a[i] += d
        if (d == 1 and a[i] < M[i]) or (d == -1 and a[i] >= 0):
            yield True
        else:
            a[i] -= d
            d = -d
            yield False
