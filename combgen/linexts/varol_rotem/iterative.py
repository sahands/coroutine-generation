from combgen.helpers.permutations import move, LEFT, left_cyclic_shift
from combgen.helpers.posets import add_min_max


def varol_rotem_iterative(n, poset):
    # 0 and n + 1 will be used as the minimum and maximum
    print(n)
    poset = add_min_max(poset, 0, n + 1)
    pi = list(range(n + 2))
    inv = pi[:]

    yield pi[1:-1]
    i = n
    while i > 1:
        k = inv[i]
        if move(pi, inv, i, LEFT, poset):
            yield pi[1:-1]
            i -= 1
        else:
            left_cyclic_shift(pi, inv, inv[i], k)
            i = n
