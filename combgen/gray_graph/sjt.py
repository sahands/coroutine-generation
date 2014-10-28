from combgen.permutations.sjt.coroutine import gen_all
from .grapher import generate_pgf_gray_graph
# from gray_graph import generate_adjacency_matrix


def dist(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def neighbour(v, u):
    return dist(u, v) == 2


def to_str(a):
    return ''.join(str(x) for x in a)


def main():
    generate_pgf_gray_graph(gen_all, neighbour, to_str, 3)
    # generate_adjacency_matrix(permutations, neighbour, to_str, 3)


if __name__ == '__main__':
    main()
