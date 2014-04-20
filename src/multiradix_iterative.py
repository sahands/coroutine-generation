from __future__ import print_function

__author__ = "Sahand Saba"


def multiradix(M):
    """
    Generates all multiradix numbers a[m-1] ... a[0] such that
    0 <= a[i] < M[i], in lexicographic order.
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


if __name__ == '__main__':
    M = [3, 2, 3]
    for a in multiradix(M):
        print(''.join(str(x) for x in a))
