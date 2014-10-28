from combgen.helpers.permutations import transpose


def sjt_local(pi, inv, x):
    # The goal of local(pi, inv, i) is to move i permutation pi with inverse
    # permutation inv in the direction of until it hits a "barrier", defined as
    # an element smaller than it.
    d = +1
    while True:
        # j is the element next to i in pi, in direction d
        y = pi[inv[x] + d]
        if x < y:
            # Swap i and j
            transpose(pi, inv, x, y)
            yield True
        else:
            # Change direction and yield False
            d = -d
            yield False
