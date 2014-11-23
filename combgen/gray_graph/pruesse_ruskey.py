from combgen.linexts.pruesse_ruskey.coroutine import gen_all
from combgen.linexts.pruesse_ruskey.coroutine import tests
from .grapher import generate_pgf_gray_graph
# from gray_graph import generate_adjacency_matrix


def dist(a, b):
    # d = 1 if a[0] != b[0] else 0
    # return d + sum(abs(x - y) for x, y in zip(a[1:], b[1:]))
    return sum(abs(x - y) for x, y in zip(a, b))


def neighbour(v, u):
    return dist(u, v) == 2


def to_str(a):
    return '"${}{}$"'.format('-' if a[0] < 0 else '+', ''.join(str(x) for x in a[1:]))


def main():
    generate_pgf_gray_graph(gen_all, neighbour, to_str, 4, tests.poset, tests.a_b_pairs)
    # generate_adjacency_matrix(permutations, neighbour, to_str, 3)


if __name__ == '__main__':
    main()
