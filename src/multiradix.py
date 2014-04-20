from __future__ import print_function


from nobody import nobody
from utils import log_execution_time

__author__ = "Sahand Saba"


def multiradix_recursive(M):
    """
    Generates all multiradix numbers a[m-1] ... a[0] such that
    0 <= a[i] < M[i], in lexicographic order using a recursive algorithm.
    """
    n = len(M)
    a = [0] * n

    def gen(i):
        if i < 0:
            yield a
            return

        for __ in gen(i - 1):
            for x in range(M[i]):
                a[i] = x
                yield a

    return gen(n - 1)


def multiradix_coroutine_core(M):
    """
    Generates all multiradix numbers a[m-1] ... a[0] such that
    0 <= a[i] < M[i], in lexicographic order using coroutines.
    """
    # The idea is simple here: create a coroutine gen(i)
    # whose task is to check if a[i] < M[i] - 1 in which
    # case just increase a[i] and yield a[i] == M[i]
    # otherwise set a[i] = 0 and yield gen(i - 1)
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
    a, lead = multiradix_coroutine_core(M)
    while next(lead):
        yield a


def multiradix_iterative(M):
    """
    Generates all multiradix numbers a[m-1] ... a[0] such that
    0 <= a[i] < M[i], in lexicographic order using an iterative algorithm.
    """
    n = len(M)
    a = [0] * n
    while True:
        yield a
        # Find the first index that can be increased by scanning from the right
        # to left, and setting everything to zero until we find what we are
        # looking for.
        k = n - 1
        while k >= 0 and a[k] == M[k] - 1:
            a[k] = 0
            k -= 1
        if k < 0:
            # Nothing could be increased, so we are at last lexicographic item
            break
        # Increase it
        a[k] += 1


@log_execution_time
def run_test(generator):
    M = [10] * 7
    for a in generator(M):
        pass


def basic_test(generator):
    M = [3, 2, 3]
    for a in generator(M):
        print(''.join(str(x) for x in a))


if __name__ == '__main__':
    for generator in [multiradix_coroutine,
                      multiradix_iterative,
                      multiradix_recursive]:
        print('Testing {}:'.format(generator.__name__))
        run_test(generator)
        print()
