from time import sleep


def nobody():
    while True:
        yield False


def troll(i, n, pi, inv):
    """
    The goal of troll[i] is to move i in the direction of until it hits a
    "barrier", defined as an element smaller than it.
    """
    neighbour = troll(i + 1, n, pi, inv) if i < n else nobody()
    d = 1
    while True:
        # j is the element next to i in pi, in direction d
        j = pi[inv[i] + d]
        if i < j:
            # Swap i and j
            pi[inv[i]], pi[inv[j]] = j, i
            inv[i], inv[j] = inv[j], inv[i]
            yield True
        else:
            # Change direction and poke
            d = -d
            yield next(neighbour)


def setup(n):
    # Start with the identity permutation with 0 padded on both sides
    # Example: for n = 4, pi starts as [0, 1, 2, 3, 4, 0]
    # The zeros act as "fixed barriers", never moving
    pi = list(range(n + 1)) + [0]

    # The inverse permutation starts as the identity as well.
    inv = pi[:-1]

    # The lead coroutine will be the
    # item n in the permutation
    lead = troll(1, n, pi, inv)
    return pi, lead


def permutations(n):
    pi, lead = setup(n)
    yield pi[1:-1]
    while next(lead):
        yield pi[1:-1]


def main():
    n = 3
    pi, lead = setup(n)
    while True:
        print(pi[1:-1])
        if not next(lead):
            print('----')
            sleep(1)


if __name__ == '__main__':
    main()
