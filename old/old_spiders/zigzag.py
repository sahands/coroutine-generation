from time import sleep

from zigzag_coroutine import setup


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
