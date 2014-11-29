from .product import pruesse_ruskey_product
from .barrier import pruesse_ruskey_barrier

# Print debug messages or not
DEBUG = False


def setup(n, poset, a_b_pairs):
    pi = list(range(n + 1))
    inv = pi[:]
    pi[0] = 1
    Y = pruesse_ruskey_barrier()
    for a, b in reversed(a_b_pairs):
        Y = pruesse_ruskey_product(poset, pi, inv, a, b, Y)
    return Y, pi
