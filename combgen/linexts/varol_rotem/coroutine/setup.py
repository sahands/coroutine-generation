from .local import varol_rotem_local
from combgen.common import barrier, stitch_coroutines
from combgen.helpers.posets import add_min_max


def setup(n, poset):
    # 0 and n + 1 will be used as the minimum and maximum
    poset = add_min_max(poset, 0, n + 1)
    pi = list(range(n + 2))
    inv = pi[:]
    coroutines = [varol_rotem_local(poset, pi, inv, i + 1) for i in range(n)]
    coroutines.append(barrier())
    lead = stitch_coroutines(coroutines)
    return lead, pi
