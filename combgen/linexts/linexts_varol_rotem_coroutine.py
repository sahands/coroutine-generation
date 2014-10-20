from nobody import nobody
from stitch import stitch
from permutations import move, LEFT, left_cyclic_shift


def local(poset, pi, inv, i):
    """
    Move i to the left while maintaining pi as a linear extension of poset.
    When i can no longer move to the left, do a cyclic shift to put i back to
    its starting position.
    """
    while True:
        k = inv[i]
        while move(pi, inv, i, LEFT, poset):
            yield True
        left_cyclic_shift(pi, inv, inv[i], k)
        yield False


def setup(n, poset):
    # 0 and n + 1 will be used as the minimum and maximum
    pi = list(range(n + 2))
    inv = pi[:]
    lead = nobody()
    for i in range(n):
        lead = stitch(local(poset, pi, inv, n - i), lead)
    return lead, pi
