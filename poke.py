from time import sleep
from nobody import nobody


__author__ = "Sahand Saba"
__email__ = "sahands@gmail.com"


def troll(n, k, a):
    neighbour = troll(n, k - 1, a) if k > 0 else nobody()

    while True:
        # awake:
        a[k] = 1 - a[k]
        yield True

        # asleep
        yield next(neighbour)


if __name__ == '__main__':
    n = 3
    a = [0] * n
    lead_troll = troll(n - 1, n - 1, a)
    while True:
        print(''.join(str(x) for x in a))
        if not next(lead_troll):
            print("-------")
            sleep(1)
