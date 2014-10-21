from .gen_all import gen_all


def main():
    def poset(x, y):
        R = {(1, 3), (2, 4)}
        return (x, y) in R

    n = 4
    a_b_pairs = [(1, 2), (3, 4)]
    S = set()
    for pi in gen_all(n, poset, a_b_pairs):
        # d = ["", "1", "a", "2", "b"]
        d = ["", "1", "2", "3", "4"]
        s = ("+" if pi[0] > 0 else "-") + ''.join(d[x] for x in pi[1:])
        print(s)
        if s in S:
            print("DUPLICATE - something went wrong!")
        S.add(tuple(pi))
    print(len(S))


if __name__ == '__main__':
    main()
