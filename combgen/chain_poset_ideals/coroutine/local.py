def chain_poset_ideals_local(a, i):
    while True:
        a[i] = 1 - a[i]
        yield True
        yield False
