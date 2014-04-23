from __future__ import print_function


def gray(n):
    if n > 0:
        g = gray(n - 1)
        gr = reversed(g)
        return (['0' + a for a in g] +
                ['1' + a for a in gr])
    else:
        return ['']
