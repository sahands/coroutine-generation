from __future__ import print_function

from time import sleep

from sjt_coroutine import permutations
from sjt_coroutine import setup

__author__ = "Sahand Saba"


def cyclic_test(n):
    pi, lead = setup(n)
    c = 0
    while True:
        print(''.join(str(x) for x in pi[1:-1]))
        c += 1
        if not next(lead):
            print('-------')
            print(c)
            print('-------')
            sleep(1)
            c = 0


if __name__ == '__main__':
    print('\n'.join(''.join(str(x) for x in pi) for pi in permutations(1)))
    print('\n'.join(''.join(str(x) for x in pi) for pi in permutations(2)))
    print('\n'.join(''.join(str(x) for x in pi) for pi in permutations(3)))
    print('\n'.join(''.join(str(x) for x in pi) for pi in permutations(4)))
    cyclic_test(3)
