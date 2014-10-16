from multiradix_coroutine import multiradix_coroutine
from multiradix_gray_coroutine import multiradix_gray_coroutine
from gen_graph import generate_pgf_gray_graph


def dist(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def neighbour(u, v):
    return dist(u, v) == 1


def to_str(a):
    return ''.join(str(x) for x in a)


def main():
    M = [3, 2, 3]
    generate_pgf_gray_graph(multiradix_coroutine, neighbour, to_str, M)
    print()
    print()
    generate_pgf_gray_graph(multiradix_gray_coroutine, neighbour, to_str, M)


if __name__ == '__main__':
    main()
