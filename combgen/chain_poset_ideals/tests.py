from combgen.common import cosymsum, coproduct
from combgen.chain_poset_ideals.coroutine import chain_poset_ideals_local as X
from combgen.chain_poset_ideals.coroutine import gen_all, setup


def manual_setup_test():
    n = 6
    a = [0] * n
    lead = coproduct(cosymsum(X(a, 1), X(a, 0)),
                     X(a, 2),
                     cosymsum(X(a, 5), X(a, 4), X(a, 3)))
    k = 0
    c = 0
    while True:
        k += 1
        print(''.join(str(x) for x in a))
        if not next(lead):
            print('--', k, '--')
            k = 0
            c += 1
            if c > 1:
                break


def cyclic_test():
    n = 6
    E = [-1, 1, 2, 5]
    a, lead = setup(n, E)
    c = 0
    while True:
        print(''.join(str(x) for x in a))
        if not next(lead):
            print('---')
            c += 1
            if c > 2:
                break


def auto_setup_test():
    # The "heads" of the chains 0 < *1*, *2* stand-alone, and 3 < 4 < *5*
    n = 6
    E = [-1, 1, 2, 5]
    A = list(a[:] for a in gen_all(n, E))
    for a in A:
        print(''.join(str(x) for x in a))
    print('--', len(A), '--')


def main():
    manual_setup_test()
    auto_setup_test()
    cyclic_test()


if __name__ == '__main__':
    main()
