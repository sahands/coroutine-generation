from combgen.helpers.posets.zigzag import zigzag
from .local import SWITCH_SIGN
from .setup import setup
from .gen_all import gen_all
from .gen_all_no_sign import gen_all_no_sign


n = 4
a_b_pairs = [(1, 2), (3, 4)]


def poset(x, y):
    R = {(1, 3), (2, 4)}
    return (x, y) in R


def to_str(pi):
    s = ("+" if pi[0] > 0 else "-") + ''.join(str(x) for x in pi[1:])
    return '{}'.format(s)


def cyclic_test(n, poset, a_b_pairs, k):
    lead, pi = setup(n, poset, a_b_pairs)
    t = 0
    print('------')
    S = set()
    while True:
        s = to_str(pi)
        S.add(s)
        print(s)
        result = next(lead)
        if not result:
            t += 1
            print('--')
            print(len(S))
            print('--')
            S = set()
            if t > k:
                print('------')
                return
        if result == SWITCH_SIGN:
            pi[0] = -pi[0]


def gen_all_test():
    S = set()
    for pi in gen_all(n, poset, a_b_pairs):
        s = to_str(pi)
        print(s)
        if s in S:
            print("DUPLICATE - something went wrong!")
        S.add(tuple(pi))
    print(len(S))


def gen_all_no_sign_test():
    S = set()
    for pi in gen_all_no_sign(n, poset, a_b_pairs):
        s = ''.join(str(x) for x in pi)
        print(s)
        if s in S:
            print("DUPLICATE - something went wrong!")
        S.add(tuple(pi))
    print(len(S))


def test_zig_zag():
    n = 5
    poset = zigzag(n)
    a_b_pairs = [(1, 2), (3, 4)]
    S = set()
    for pi in gen_all(n, poset, a_b_pairs):
        s = to_str(pi)
        print(s)
        if s in S:
            print("DUPLICATE - something went wrong!")
        S.add(s)
    print(len(S))


# Number of linear extensions of the zig-zag poset: http://oeis.org/A000111
A000111 = [1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936, 50521, 353792]


def test_against_A000111(n):
    poset = zigzag(n)
    if n <= 2:
        a_b_pairs = []
    else:
        a_b_pairs = [(2 * i - 1, 2 * i) for i in range(1, n // 2 + 1)]
    L = [pi[:] for pi in gen_all_no_sign(n, poset, a_b_pairs)]
    S = set(tuple(pi) for pi in L)
    T = (len(L), len(S), A000111[n])
    print(T)
    if len(set(T)) > 1:
        print("WARNING: Zigzag poset linear extensions "
              "were not correctly generated.")


def main():
    gen_all_test()
    gen_all_no_sign_test()
    cyclic_test(n, poset, a_b_pairs, 3)
    test_zig_zag()
    for m in range(len(A000111)):
        test_against_A000111(m)


if __name__ == '__main__':
    main()
