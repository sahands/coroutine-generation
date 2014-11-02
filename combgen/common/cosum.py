def cosum(*Xs):
    # Produce pattern (X_1 X_2 X_3 ... |)*
    # "co" stands for coroutine... not to be confused with Category Theory dual
    # concepts of cosum, coproduct, etc...
    while True:
        for X in Xs:
            while next(X):
                yield True
        yield False
