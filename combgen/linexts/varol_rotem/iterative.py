from combgen.helpers.permutations import move, LEFT, left_cyclic_shift
from combgen.helpers.posets import add_min_max


def gen_all(n, poset):
    # 0 and n + 1 will be used as the minimum and maximum
    poset = add_min_max(poset, 0, n + 1)
    pi = list(range(n + 2))
    inv = pi[:]
    yield pi[1:-1]
    x = n
    while x > 1:
        if move(pi, inv, x, LEFT, poset):
            yield pi[1:-1]
            x = n
        else:
            left_cyclic_shift(pi, inv, inv[x], x)
            x -= 1
