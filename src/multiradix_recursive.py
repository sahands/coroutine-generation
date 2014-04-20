from __future__ import print_function

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


if __name__ == '__main__':
    M = [3, 2, 3]
    for a in multiradix(M):
        print(''.join(str(x) for x in a))
