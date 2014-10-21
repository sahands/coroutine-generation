from combgen.common import nobody, stitch_coroutines
from .local import local


def setup(M):
    n = len(M)
    a = [0] * n
    coroutines = [local(M, a, i) for i in range(n)] + [nobody()]
    lead = stitch_coroutines(coroutines)
    return a, lead
