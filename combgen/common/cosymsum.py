from combgen.common import cosum, cojoin


def cosymsum(*Xs):
    # Produce pattern (X_1 X_2 X_3 ... X_n | X_n X_{n-1} X_{n-2} ... X_1 |)*
    XY = cosum(*Xs)
    YX = cosum(*reversed(Xs))
    return cojoin(XY, YX)
