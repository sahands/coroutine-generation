from .stitch import pruesse_ruskey_stitch
from .nobody import pruesse_ruskey_nobody

# Print debug messages or not
DEBUG = False


def setup(n, poset, a_b_pairs):
    pi = list(range(n + 1))
    inv = pi[:]
    pi[0] = 1
    lead = pruesse_ruskey_nobody()
    for a, b in reversed(a_b_pairs):
        lead = pruesse_ruskey_stitch(n, poset, pi, inv, a, b, lead)
    return lead, pi
