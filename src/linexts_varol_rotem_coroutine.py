from nobody import nobody
from stitch import stitch
from permutation_move import move, LEFT
from time import sleep


def cyclic_shift(pi, inv, start, end):
    # print("Shifting {} to {}".format(start, end))
    i = pi[start]
    for k in range(start, end):
        t = pi[k + 1]
        inv[t] -= 1
        pi[k] = t
    inv[i] = end
    pi[end] = i


def local(poset, pi, inv, i):
    """
    Move i to the left while maintaining pi as a linear extension of poset.
    When i can no longer move to the left, do a cyclic shift to put i back to
    the its starting position.
    """
    while True:
        k = inv[i]
        # print("i = {}, k = {}".format(i, k))
        while move(pi, inv, i, LEFT, poset):
            # print("moved {} to the left".format(i))
            # print(pi)
            yield True
            # sleep(1)
        # Can not move i to the left anymore, do cyclic shift of pi[i] to pi[k]
        # print(pi[1:-1])
        # print(inv[1:-1])
        cyclic_shift(pi, inv, inv[i], k)
        # print(pi[1:-1])
        # print(inv[1:-1])
        sleep(1)
        yield False


def setup(n, poset):
    pi = list(range(n + 2))
    inv = pi[:]
    lead = nobody()
    for i in range(n):
        lead = stitch(local(poset, pi, inv, n - i), lead)
    return lead, pi
