from combgen.common import cosymsum, coproduct
from combgen.chain_poset_ideals.coroutine import chain_poset_ideals_local as X
from combgen.chain_poset_ideals.coroutine import setup


def run_test(a, lead, repetitions=1):
    k = 0
    c = 0
    while True:
        k += 1
        print(''.join(str(x) for x in a))
        if not next(lead):
            print('--', k, '--')
            k = 0
            c += 1
            if c > repetitions:
                break


def tree_test():
    n = 8
    a = [0] * n
    C1 = cosymsum(X(a, 1), X(a, 2))
    C5 = cosymsum(X(a, 5), X(a, 6))
    C4 = coproduct(X(a, 4), C5)
    C3 = cosymsum(X(a, 3), C4)
    Z = coproduct(C1, C3, X(a, 7))
    lead = cosymsum(X(a, 0), Z)
    run_test(a, lead)


def manual_setup_test():
    n = 6
    a = [0] * n
    lead = coproduct(cosymsum(X(a, 0), X(a, 1)),
                     X(a, 2),
                     cosymsum(X(a, 3), X(a, 4), X(a, 5)))
    run_test(a, lead)


def auto_setup_test():
    # The "heads" of the chains 0 < *1*, *2* stand-alone, and 3 < 4 < *5*
    n = 6
    E = [-1, 1, 2, 5]
    a, lead = setup(n, E)
    run_test(a, lead)


def main():
    tree_test()
    manual_setup_test()
    auto_setup_test()


if __name__ == '__main__':
    main()
