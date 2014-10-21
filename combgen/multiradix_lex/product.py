from itertools import product


def gen_all(M):
    return product(*(range(x) for x in M))
