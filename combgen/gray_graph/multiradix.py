from combgen.multiradix_gray.coroutine import gen_all
from .grapher import generate_pgf_gray_graph


def dist(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def neighbour(u, v):
    return dist(u, v) == 1


def to_str(a):
    return '"${}$"'.format(''.join(str(x) for x in a))


def main():
    M = [3, 2, 3]
    generate_pgf_gray_graph(gen_all, neighbour, to_str, M)
    # print()
    # print()
    # generate_pgf_gray_graph(multiradix_gray_coroutine, neighbour, to_str, M)


if __name__ == '__main__':
    main()
