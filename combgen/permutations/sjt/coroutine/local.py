from combgen.helpers.permutations import transpose


def sjt_local(pi, inv, i):
    # The goal of local(pi, inv, i) is to move i permutation pi with inverse
    # permutation inv in the direction of until it hits a "barrier", defined as
    # an element smaller than it.
    d = +1
    while True:
        # j is the element next to i in pi, in direction d
        j = pi[inv[i] + d]
        if i < j:
            # Swap i and j
            transpose(pi, inv, i, j)
            yield True
        else:
            # Change direction and yield False
            d = -d
            yield False

