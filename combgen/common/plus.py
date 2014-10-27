def X_plus_Y(X, Y):
    while True:
        while next(X):
            yield True
        yield False
        while next(Y):
            yield True
        yield False
