def stitch(X, Y):
    while True:
        while next(Y):
            yield True
        yield next(X)

