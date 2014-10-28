from combgen.common import stitch_coroutines
from .local import multiradix_gray_local


def setup(M):
    n = len(M)
    a = [0] * n
    coroutines = [multiradix_gray_local(M, a, i) for i in range(n)]
    lead = stitch_coroutines(coroutines)
    return a, lead
