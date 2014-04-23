from itertools import product


def multiradix_product(M):
    return product(*(range(x) for x in M))
