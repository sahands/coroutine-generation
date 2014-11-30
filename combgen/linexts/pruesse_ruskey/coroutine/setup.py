from .product import pruesse_ruskey_product
from .barrier import pruesse_ruskey_barrier


def setup(n, poset, a_b_pairs):
    pi = list(range(n + 1))
    inv = pi[:]
    pi[0] = 1
    lead = pruesse_ruskey_barrier()
    for a, b in a_b_pairs[::-1]:
        lead = pruesse_ruskey_product(poset, pi, inv, lead, a, b)
    return lead, pi
