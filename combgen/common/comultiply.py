def comultiply(X, Y):
    # Produce pattern (Y x_1 Y x_2 Y x_3 Y ... Y x_n |)*
    # Where X = x_1 x_2 x_3 ... x_n
    while True:
        while next(Y):
            yield True
        yield next(X)
