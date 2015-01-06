def cojoin(*Xs):
    while True:
        for X in Xs:
            while next(X):
                yield True
            yield False
