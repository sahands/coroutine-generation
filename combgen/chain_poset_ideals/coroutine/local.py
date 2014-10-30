DONE = False
MOVED = True


# "co" stands for coroutine... not to be confused with Category Theory dual
# concepts of cosum, coproduct, etc...
def cosum(*Xs):
    # Produce pattern (X_1 X_2 X_3 ... |)*
    while True:
        for X in Xs:
            while next(X):
                yield MOVED
        yield DONE


def cosymsum(*Xs):
    # Produce pattern (X_1 X_2 X_3 ... X_n | X_n X_{n-1} X_{n-2} ... X_1 |)*
    XY = cosum(*Xs)
    YX = cosum(*reversed(Xs))
    while True:
        while next(XY):
            yield MOVED
        yield DONE
        while next(YX):
            yield MOVED
        yield DONE


def coproduct(X, Y):
    # Produce pattern (Y x_1 Y x_2 Y x_3 Y ... Y x_n |)*
    # Where X = x_1 x_2 x_3 ... x_n
    while True:
        while next(Y):
            yield MOVED
        yield next(X)


def X(a, i):
    while True:
        a[i] = 1 - a[i]
        yield True
        yield False


def main():
    n = 5
    a = [0] * n
    # Represents the chain in which 0 < 1 and 2 < 3 < 4, corresponding to
    # multiradix numbers with base M[0] = 3 and M[1] = 4
    lead = coproduct(cosymsum(X(a, 1), X(a, 0)),
                     cosymsum(X(a, 4), X(a, 3), X(a, 2)))
    k = 0
    c = 0
    while True:
        k += 1
        print(''.join(str(x) for x in a))
        if not next(lead):
            print('--', k, '--')
            k = 0
            c += 1
            if c > 1:
                break


if __name__ == '__main__':
    main()

# Output:
# 00000
# 00001
# 00011
# 00111
# 01111
# 01011
# 01001
# 01000
# 11000
# 11001
# 11011
# 11111
# -- 12 --
# 11111
# 11011
# 11001
# 11000
# 01000
# 01001
# 01011
# 01111
# 00111
# 00011
# 00001
# 00000
# -- 12 --
