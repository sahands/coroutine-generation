from combgen.linexts.varol_rotem import coroutine
from combgen.linexts.varol_rotem import iterative
from combgen.helpers.posets import zigzag


def test_alg(n, gen_all):
    poset = zigzag(n)
    for c, pi in enumerate(gen_all(n, poset)):
        print(c + 1, ''.join(str(x) for x in pi))


def main():
    n = 6
    test_alg(n, coroutine.gen_all)
    print('----')
    test_alg(n, iterative.gen_all)


if __name__ == '__main__':
    main()
