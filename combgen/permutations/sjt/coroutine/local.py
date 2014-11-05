from combgen.helpers.permutations import transpose


def sjt_local(pi, inv, x):
    # The goal of local(pi, inv, i) is to move i permutation pi with inverse
    # permutation inv in the direction of until it hits a "barrier", defined as
    # an element greater than it.
    d = -1
    while True:
        y = pi[inv[x] + d]  # y is the element next to x in direction d
        if x < y:
            d = -d  # Switch direction
            yield False
        else:
            transpose(pi, inv, x, y)
            yield True
