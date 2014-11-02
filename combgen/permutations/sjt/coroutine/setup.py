from combgen.common import coproduct
from .local import sjt_local


def setup(n):
    # Start with the identity permutation with 0 padded on both sides
    # Example: for n = 4, pi starts as [0, 1, 2, 3, 4, 0]
    # The n + 1 at the beginning and end will act as "fixed barriers", never
    # moving
    pi = [n + 1] + list(range(1, n + 1)) + [n + 1]
    # The inverse permutation starts as the identity as well. It does not need
    # the fixed barriers since their inverses will never be looked up.
    inv = pi[:-1]
    # The lead coroutine will be the coroutine in charge of moving n
    coroutines = [sjt_local(pi, inv, i + 1) for i in range(n)]
    lead = coproduct(*coroutines)
    return pi, lead
