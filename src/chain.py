from time import sleep

from chain_coroutine import setup


if __name__ == '__main__':
    n = 6
    E = [0, 2, 3]
    a, lead_troll = setup(E, n)
    count = 0
    while True:
        count += 1
        print(''.join(str(x) for x in a))
        if not next(lead_troll):
            print("----- Count = {0} -----".format(count))
            count = 0
            sleep(1)
