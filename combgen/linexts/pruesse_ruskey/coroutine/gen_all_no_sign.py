from .gen_all import gen_all


def gen_all_no_sign(n, poset, a_b_pairs):
    for i, pi in enumerate(gen_all(n, poset, a_b_pairs)):
        if i % 2 == 0:
            yield pi[1:]
