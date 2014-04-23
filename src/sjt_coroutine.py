from nobody import nobody


def troll(pi, inv, i):
    previous = troll(pi, inv, i - 1) if i > 1 else nobody()
    d = -1
    while True:
        j = inv[i]
        if pi[j] < pi[j + d]:
            d = -d
            yield next(previous)
        else:
            pi[j], pi[j + d] = pi[j + d], pi[j]
            inv[i] += d
            inv[pi[j]] -= d
            yield True


def setup(n):
    # Start with the identity permutation with n + 2 padded on both sides
    pi = list(range(1, n + 1))
    pi = [n + 2] + pi + [n + 2]
    # The inverse permutation starts as the identity as well.
    inv = pi[:-1]

    # The lead coroutine will be the
    # item n in the permutation
    lead = troll(pi, inv, n)
    return pi, lead


def permutations(n):
    pi, lead = setup(n)
    yield pi[1:-1]
    while next(lead):
        yield pi[1:-1]
