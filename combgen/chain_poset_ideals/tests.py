from combgen.common import cosymsum, coproduct
from combgen.chain_poset_ideals.coroutine import chain_poset_ideals_local as X
from combgen.chain_poset_ideals.coroutine import gen_all


def manual_setup_test():
    n = 5
    a = [0] * n
    # First, manually:
    # Represents the chain in which 0 < 1 and 2 < 3 < 4, corresponding to
    # multiradix numbers with base M[0] = 3 and M[1] = 4
    lead = coproduct(cosymsum(X(a, 1), X(a, 0)),
                     cosymsum(X(a, 4), X(a, 3), X(a, 2)))
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


def auto_setup_test():
    n = 5
    E = [1, 4]  # The "heads" of the chains 0 < *1* and 2 < 3 < *4*
    A = list(a[:] for a in gen_all(n, E))
    for a in A:
        print(''.join(str(x) for x in a))
    print('--', len(A), '--')


def main():
    manual_setup_test()
    auto_setup_test()


if __name__ == '__main__':
    main()
