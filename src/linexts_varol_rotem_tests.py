from time import sleep
from linexts_varol_rotem_coroutine import setup
from posets import zig_zag, add_min_max


def test(n, M=None):
    # z = zig_zag(n)
    # poset = add_min_max(z, 0, n + 1)
    poset = add_min_max(lambda a, b: False, 0, n + 1)
    c = 0
    lead, pi = setup(n, poset)
    while True:
        c += 1
        print(c, ''.join(str(x) for x in pi[1:-1]))
        if not next(lead):
            print('-----')
            sleep(1)


def main():
    test(3)

if __name__ == '__main__':
    main()
