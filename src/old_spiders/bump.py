from time import sleep
from nobody import nobody


__author__ = "Sahand Saba"
__email__ = "sahands@gmail.com"


def troll(n, k, a):
    neighbour = troll(n, k + 1, a) if k < n else nobody()

    while True:
        # awake0:
        while next(neighbour):
            yield True
        a[k] = 1
        yield True

        # asleep1:
        yield False

        # awake1:
        a[k] = 0
        yield True

        # asleep0
        while next(neighbour):
            yield True
        yield False


if __name__ == '__main__':
    n = 3
    a = [0] * n
    lead_troll = troll(n - 1, 0, a)
    while True:
        print(''.join(str(x) for x in a))
        if not next(lead_troll):
            print("-------")
            sleep(1)
