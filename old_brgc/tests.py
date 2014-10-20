from __future__ import print_function

from time import sleep

from bgrc_coroutine import gray
from bgrc_coroutine import setup


__author__ = "Sahand Saba"
__email__ = "sahands@gmail.com"


def cyclical_test(n):
    a, lead_coroutine = setup(n)
    while True:
        print(''.join(str(x) for x in a))
        if not next(lead_coroutine):
            print("-------")
            sleep(1)


def main():
    for a in gray(3):
        print(''.join(str(x) for x in a))
    # cyclical_test(3)

if __name__ == '__main__':
    main()
