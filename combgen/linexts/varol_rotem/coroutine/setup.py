from .local import local
from combgen.common import nobody, stitch_coroutines
from combgen.helpers.posets import add_min_max


def setup(n, poset):
    # 0 and n + 1 will be used as the minimum and maximum
    poset = add_min_max(poset, 0, n + 1)
    pi = list(range(n + 2))
    inv = pi[:]
    coroutines = [local(poset, pi, inv, i + 1) for i in range(n)] + [nobody()]
    lead = stitch_coroutines(coroutines)
    return lead, pi
