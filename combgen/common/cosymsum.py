from combgen.common import cosum


def cosymsum(*Xs):
    # Produce pattern (X_1 X_2 X_3 ... X_n | X_n X_{n-1} X_{n-2} ... X_1 |)*
    XY = cosum(*Xs)
    YX = cosum(*reversed(Xs))
    while True:
        while next(XY):
            yield True
        yield False
        while next(YX):
            yield True
        yield False
