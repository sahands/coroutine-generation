from time import sleep


def nobody():
    while True:
        yield False


def setup(n):
    # Start with the identity permutation with 0 padded on both sides
    # Example: for n = 4, pi starts as [0, 1, 2, 3, 4, 0]
    # The zeros act as "fixed barriers", never moving
    pi = list(range(n + 1)) + [0]

    # The inverse permutation starts as the identity as well. It does not need
    # the fixed barriers since their inverses will never be looked up.
    inv = pi[:-1]

    def troll(i):
        """
        The goal of troll[i] is to move i in the direction of until it hits a
        "barrier", defined as an element smaller than it.
        """
        neighbour = troll(i + 1) if i < n else nobody()
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

    # The lead coroutine will be the coroutine in charge of moving 1
    return pi, troll(1)


def permutations(n):
    pi, lead = setup(n)
    yield pi[1:-1]
    while next(lead):
        yield pi[1:-1]


def main():
    s = set()
    n = 4
    pi, lead = setup(n)
    while True:
        s.add(tuple(pi[1:-1]))
        print(pi[1:-1])
        if not next(lead):
            print('----', len(s), '----')
            sleep(1)
            s.clear()


if __name__ == '__main__':
    main()
