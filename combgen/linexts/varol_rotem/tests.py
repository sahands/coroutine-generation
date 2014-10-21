from combgen.linexts.varol_rotem.coroutine import setup
from combgen.linexts.varol_rotem.iterative import varol_rotem_iterative
from combgen.helpers.posets import zigzag


def test_coroutine(n):
    poset = zigzag(n)
    c = 0
    lead, pi = setup(n, poset)
    while True:
        c += 1
        print(c, ''.join(str(x) for x in pi[1:-1]))
        if not next(lead):
            return


def test_iterative(n):
    poset = zigzag(n)
    for c, pi in enumerate(varol_rotem_iterative(n, poset)):
        print(c + 1, ''.join(str(x) for x in pi))


def main():
    n = 6
    test_coroutine(n)
    print('----')
    test_iterative(n)


if __name__ == '__main__':
    main()
