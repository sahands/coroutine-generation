from .local import SWITCH_SIGN
from .setup import setup


def gen_all(n, poset, a_b_pairs):
    lead, pi = setup(n, poset, a_b_pairs)
    yield pi
    for result in lead:
        if not result:
            return
        if result is SWITCH_SIGN:
            pi[0] = -pi[0]
        yield pi
