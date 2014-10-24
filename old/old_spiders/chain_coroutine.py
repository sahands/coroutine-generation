from barrier import barrier


def troll(E, n, i, a):
    above = barrier()
    prev_lead = barrier()
    if i + 1 not in (E + [n + 1]):
        above = troll(E, n, i + 1, a)
    if i in E and i != 0:
        prev_lead = troll(E, n, E[E.index(i) - 1], a)

    while True:
        # Awake and light off - a[i] = 0
        while next(above):
            yield True
        a[i] = 1
        yield True

        # Asleep and light on - a[i] = 1
        yield next(prev_lead)

        # Awake and light on - a[i] = 1
        a[i] = 0
        yield True

        # Asleep and light off - a[i] = 0
        while next(above):
            yield True
        yield next(prev_lead)


def setup(E, n):
    a = [0] * n
    lead_troll = troll(E, n - 1, E[-1], a)
    return a, lead_troll
