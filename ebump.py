from time import sleep
from nobody import nobody


__author__ = "Sahand Saba"
__email__ = "sahands@gmail.com"


def troll(E, n, k, a):
    above = troll(E, n, k + 1, a) if k + 1 not in (E + [n + 1]) else nobody()
    prev_lead = troll(E, n, E[E.index(k) - 1], a) if k in E and k != 0 else nobody()

    while True:
        # awake0:
        while next(above):
            yield True
        a[k] = 1
        yield True

        # asleep1
        yield next(prev_lead)

        # awake1:
        a[k] = 0
        yield True

        # asleep0:
        while next(above):
            yield True
        yield next(prev_lead)


if __name__ == '__main__':
    n = 6
    E = [0, 2, 3]  # a[0] <= a[1], a[3] <= a[4] <= ... <= a[n - 1]
    # E = [0]  # This means a[0] <= a[1] <= a[2] <= ... <= a[n - 1]
    # E = range(n)  # This means no constraints


    count = 0
    a = [0] * n
    lead_troll = troll(E, n - 1, E[-1], a)
    while True:
        count += 1
        print(''.join(str(x) for x in a))
        if not next(lead_troll):
            print("----- Count = {0} -----".format(count))
            count = 0
            sleep(1)

