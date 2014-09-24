from varol_rotem import exts


def dist(p, q):
    """Given permutations p and q of 0, 1, ..., n - 1 where n = len(p) =
    len(q), find the minimal number of transpositions to go from p to q."""
    return sum(1 for x, y in zip(p, q) if x != y)


def main():
    extensions = list(exts(4, lambda a, b: b == 4))

    print extensions


if __name__ == '__main__':
    main()
