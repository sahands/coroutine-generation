def sjt(a):
    if a:
        r = list(range(len(a)))
        for pi in sjt(a[:-1]):
            for i in r:
                yield pi[i:] + [a[-1]] + pi[:i]
            r.reverse()
    else:
        yield []

for pi in sjt([1, 2, 3]):
    print(pi)
