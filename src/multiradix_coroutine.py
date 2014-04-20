from __future__ import print_function

from nobody import nobody

__author__ = "Sahand Saba"


def multiradix(M):
    """
    Generates all multiradix numbers a[m-1] ... a[0] such that
    0 <= a[i] < M[i], in lexicographic order.
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


if __name__ == '__main__':
    M = [3, 2, 3]
    a, lead = multiradix(M)
    while next(lead):
        print(''.join(str(x) for x in a[1:]))
