def gen_all(n):
    if n:
        r = list(range(n))
        for pi in gen_all(n - 1):
            for i in r:
                yield pi[i:] + [n] + pi[:i]
            r.reverse()
    else:
        yield []
