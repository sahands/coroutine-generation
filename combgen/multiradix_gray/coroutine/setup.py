from combgen.common import barrier
from combgen.common import stitch_coroutines
from .local import local


def setup(M):
    n = len(M)
    a = [0] * n
    coroutines = [local(M, a, i) for i in range(n)] + [barrier()]
    lead = stitch_coroutines(coroutines)
    return a, lead
