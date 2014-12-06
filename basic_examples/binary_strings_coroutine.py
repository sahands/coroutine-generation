def troll(a, i=None, neighbour=None):
    while True:
        if neighbour is None:
            yield False  # If last troll in line, just yell "done"
        else:
            a[i] = 1  # Wake up
            yield True  # Yell "moved"
            a[i] = 0  # Go to sleep
            yield next(neighbour)  # Poke neighbour
