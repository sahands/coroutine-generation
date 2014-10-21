from combgen.common import nobody, stitch_coroutines
from combgen.helpers.permutations import move, LEFT, left_cyclic_shift
from combgen.helpers.posets import add_min_max


def local(poset, pi, inv, i):
    # Move i to the left while maintaining pi as a linear extension of poset.
    # When i can no longer move to the left, do a cyclic shift to put i back to
    # its starting position.
    while True:
        while move(pi, inv, i, LEFT, poset):
            yield True
        left_cyclic_shift(pi, inv, inv[i], i)
        yield False


def setup(n, poset):
    # 0 and n + 1 will be used as the minimum and maximum
    poset = add_min_max(poset, 0, n + 1)
    pi = list(range(n + 2))
    inv = pi[:]
    coroutines = [local(poset, pi, inv, i + 1) for i in range(n)] + [nobody()]
    lead = stitch_coroutines(coroutines)
    return lead, pi
