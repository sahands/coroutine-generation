from combgen.common import barrier, stitch_coroutines
from .local import sjt_local


def setup(n):
    # Start with the identity permutation with 0 padded on both sides
    # Example: for n = 4, pi starts as [0, 1, 2, 3, 4, 0]
    # The zeros act as "fixed barriers", never moving
    pi = list(range(n + 1)) + [0]
    # The inverse permutation starts as the identity as well. It does not need
    # the fixed barriers since their inverses will never be looked up.
    inv = pi[:-1]
    # The lead coroutine will be the coroutine in charge of moving 1
    coroutines = [sjt_local(pi, inv, n - i) for i in range(n)]
    coroutines.append(barrier())
    lead = stitch_coroutines(coroutines)
    return pi, lead
