from .gen_all import gen_all


a_b_pairs = [(1, 2), (3, 4)]


def poset(x, y):
    R = {(1, 3), (2, 4)}
    return (x, y) in R


def to_str(pi):
    # d = ["", "1", "a", "2", "b"]
    d = ["", "1", "2", "3", "4"]
    # d = ["", "a_1", "a_2", "b_1", "b_2"]
    s = ("+" if pi[0] > 0 else "-") + ''.join(d[x] for x in pi[1:])
    # s = ("p" if pi[0] > 0 else "n") + ''.join(d[x] for x in pi[1:])
    # return '"${}$"'.format(s)
    return '{}'.format(s)


def main():
    n = 4
    S = set()
    for pi in gen_all(n, poset, a_b_pairs):
        s = to_str(pi)
        print(s)
        if s in S:
            print("DUPLICATE - something went wrong!")
        S.add(tuple(pi))
    print(len(S))


if __name__ == '__main__':
    main()
