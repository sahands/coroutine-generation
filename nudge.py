from time import sleep
from nobody import nobody

__author__ = "Sahand Saba"
__email__ = "sahands@gmail.com"


def troll(n, k, a, trolls):
    next_up = trolls[k + 1] if k + 1 < n else nobody()
    next_down = trolls[k + 2] if k + 2 < n else nobody()

    if a[k] == 1 or k % 2 == 1:
        next_up, next_down = next_down, next_up

    while True:
        # awake
        while next(next_up):
            yield True
        a[k] = 1 - a[k]
        yield True

        # asleep
        while next(next_down):
            yield True
        yield False

        next_up, next_down = next_down, next_up


def setup(n):
    # Initialize a to be the first n bits in 000111000111000111...
    a = ([0, 0, 0, 1, 1, 1] * (n // 6 + 1))[:n]
    trolls = []
    trolls.extend(troll(n, k, a, trolls) for k in range(n))
    trolls[0]
    return a, trolls[0]


def cyclic_test(n):
    a, lead = setup(n)
    count = 0
    while True:
        count += 1
        print(''.join(str(x) for x in a))
        if not next(lead):
            print("----- Count = {0} -----".format(count))
            count = 0
            sleep(1)


if __name__ == '__main__':
    cyclic_test(5)
