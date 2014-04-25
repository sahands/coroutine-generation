from operator import mul
from functools import reduce


def number_to_multiradix(M, x, a):
    n = len(M)
    for i in range(1, n + 1):
        x, a[-i] = divmod(x, M[-i])
    return a


def multiradix_counting(M):
    n = len(M)
    a = [0] * n
    last = reduce(mul, M, 1)
    for x in range(last):
        yield number_to_multiradix(M, x, a)
