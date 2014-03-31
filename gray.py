from time import sleep
from nobody import nobody


__author__ = "Sahand Saba"
__email__ = "sahands@gmail.com"


def gray(a, i):
    previous = gray(a, i - 1) if i > 0 else nobody()
    while True:
        a[i] = 1 - a[i]
        yield True
        yield next(previous)


def setup(n):
    a = [0] * n
    lead_coroutine = gray(a, n - 1)
    return a, lead_coroutine


if __name__ == '__main__':
    a, lead_coroutine = setup(3)
    while True:
        print(''.join(str(x) for x in a))
        if not next(lead_coroutine):
            print("-------")
            sleep(1)
