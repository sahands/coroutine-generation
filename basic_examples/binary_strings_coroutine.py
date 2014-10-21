def troll(n, a, i=None, neighbour=None):
    while True:
        if neighbour is None:
            yield False  # If last troll in line, nothing to do
        else:
            a[i] = 1
            yield True
            a[i] = 0
            yield next(neighbour)
