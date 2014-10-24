def local(a, i):
    while True:
            a[i] = 1
            yield True
            a[i] = 0
            yield False
