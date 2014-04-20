from __future__ import print_function

from utils import log_execution_time

__author__ = "Sahand Saba"


def multiradix(M):
    """
    Generates all multiradix numbers a[m-1] ... a[0] such that
    0 <= a[i] < M[i], in lexicographic order.
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


@log_execution_time
def run_test():
    M = [10] * 7
    for a in multiradix(M):
        pass
        # print(''.join(str(x) for x in a))


def basic_test():
    M = [3, 2, 3]
    for a in multiradix(M):
        print(''.join(str(x) for x in a))


if __name__ == '__main__':
    run_test()
