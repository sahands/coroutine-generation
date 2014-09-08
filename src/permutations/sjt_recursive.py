def permutations(n):
    if n:
        r = list(range(n))
        for pi in permutations(n - 1):
            for i in r:
                yield pi[i:] + [n] + pi[:i]
            r.reverse()
    else:
        yield []
