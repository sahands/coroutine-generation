from __future__ import print_function

from functools import reduce
from operator import mul

from nobody import nobody
from utils import log_execution_time

__author__ = "Sahand Saba"


def multiradix_recursive_core(M, n, a, i):
    """
    Generates all multi-radix numbers a[0] ... a[n - 1] such that
    0 <= a[i] < M[i], in lexicographic order using a recursive algorithm.
    """
    if i < 0:
        yield a
        return

    for __ in multiradix_recursive_core(M, n, a, i - 1):
        # Extend each multi-radix number of length i with all possible
        # 0 <= x < M[i] to get a multi-radix number of length i + 1.
        for x in range(M[i]):
            a[i] = x
            yield a


def multiradix_recursive(M):
    n = len(M)
    a = [0] * n
    return multiradix_recursive_core(M, n, a, n - 1)


def multiradix_coroutine_core(M):
    # The basic idea is simple here: create a coroutine gen(i) whose task is to
    # check if a[i] < M[i] - 1 in which case just increase a[i] and yield True,
    # otherwise set a[i] = 0 and yield gen(i - 1).
    n = len(M)
    M = [0] + M
    a = [0] * (n + 1)

    coroutines = [nobody()]

    def gen(i):
        while True:
            if a[i] == M[i] - 1:
                a[i] = 0
                yield next(coroutines[i - 1])
            else:
                a[i] += 1
                yield True

    coroutines.extend(gen(i) for i in range(1, n + 1))
    return a, coroutines[-1]


def multiradix_coroutine(M):
    """
    Generates all multi-radix numbers a[0] ... a[n - 1] such that
    0 <= a[i] < M[i], in lexicographic order using coroutines.
    """
    a, lead = multiradix_coroutine_core(M)
    while next(lead):
        yield a


def multiradix_iterative(M):
    """
    Generates all multi-radix numbers a[0] ... a[n - 1] such that
    0 <= a[i] < M[i], in lexicographic order using an iterative algorithm.
    """
    n = len(M)
    a = [0] * n
    while True:
        yield a
        # Find right-most index k such that a[k] < M[k] - 1 by scanning from
        # right to left, and setting everything to zero on the way.
        k = n - 1
        while a[k] == M[k] - 1:
            a[k] = 0
            k -= 1
            if k < 0:
                # Last lexicographic item
                return
        a[k] += 1


def number_to_multiradix(M, x, a):
    n = len(M)
    for i in range(1, n + 1):
        a[-i] = x % M[-i]
        x = x // M[-i]
    return a


def multiradix_counting(M):
    """
    Generates all multi-radix numbers a[0] ... a[n - 1] such that
    0 <= a[i] < M[i], in lexicographic order using arithmetic.
    """
    n = len(M)
    a = [0] * n
    last = reduce(mul, M, 1)
    for x in range(last):
        yield number_to_multiradix(M, x, a)


@log_execution_time
def test_generator(generator):
    M = [10] * 7
    for a in generator(M):
        pass


def basic_test(generator):
    M = [3, 2, 3]
    for a in generator(M):
        print(''.join(str(x) for x in a))


def run_tests():
    for generator in [multiradix_counting,
                      multiradix_iterative,
                      multiradix_recursive,
                      multiradix_coroutine]:
        print('Testing {}:'.format(generator.__name__))
        test_generator(generator)
        print()


if __name__ == '__main__':
    run_tests()
