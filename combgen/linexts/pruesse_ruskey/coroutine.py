from combgen.helpers.permutations import move, LEFT, RIGHT, transpose

# Compare results
LESS = -1
GREATER = 1
INCOMP = 0  # Incomparable

# Print debug messages or not
DEBUG = False


def setup(n, compare):
    pi = list(range(n + 1))
    inv = pi[:]
    pi[0] = 1

    def can_move_a_right(a, b):
        i = inv[a]
        if i >= n:
            return False
        right = pi[i + 1]
        return right != b and compare(a, right) == INCOMP

    def can_move_b_right(b):
        i = inv[b]
        if i >= n:
            return False
        right = pi[i + 1]
        return compare(b, right) == INCOMP

    def special_nobody():
        """Just switches the sign and yields True, then False, continuously."""
        while True:
            yield True, True
            yield False, False

    def local(a, b):
        """
        local(a, b) is a coroutine responsible for traversing the
        Hamiltonian cycle for the 2B-poset in which a is before b, followed
        immediately by the cycle in which b is before a.
        """
        while True:
            mra = mrb = 0
            # If b can not move to the right then we just move a to the right
            # as far as we can.
            if not can_move_b_right(b):
                while can_move_a_right(a, b):
                    move(pi, inv, a, RIGHT)
                    mra += 1
                    yield False, True
                # Switch sign
                yield True, True
                for __ in range(mra):
                    move(pi, inv, a, LEFT)
                    yield False, True
                yield False, False
                continue

            # Otherwise, let's start traversing the path:
            while can_move_b_right(b):
                move(pi, inv, b, RIGHT)
                mrb += 1
                yield False, True
                while can_move_a_right(a, b):
                    move(pi, inv, a, RIGHT)
                    mra += 1
                    yield False, True
                if mra > 0:
                    yield True, True
                    if mrb % 2 == 1:
                        mla = mra - 1
                    else:
                        mla = mra + 1
                    for __ in range(mla):
                        move(pi, inv, a, LEFT)
                        yield False, True
            if mra > 0 and mrb % 2 == 1:
                move(pi, inv, a, LEFT)
                yield False, True
            else:
                yield True, True
            for __ in range(mrb):
                move(pi, inv, b, LEFT)
                yield False, True
            yield False, False

    def special_stitch(a, b, t):
        u = local(a, b)
        w = local(b, a)
        while True:
            for u_change_sign, u_has_more in u:
                if not u_has_more:
                    break
                yield u_change_sign, True

            for change_sign, has_more in t:
                if not has_more:
                    break
                if change_sign:
                    if DEBUG:
                        print("Switch {} and {}".format(a, b))
                    transpose(pi, inv, a, b)
                    u, w = w, u
                    a, b = b, a
                yield False, True
                for u_change_sign, u_has_more in u:
                    if not u_has_more:
                        break
                    yield u_change_sign, True
            yield False, False

    def gen_all():
        yield pi
        lead = special_stitch(1, 2, special_stitch(3, 4, special_nobody()))
        while True:
            change_sign, has_more = next(lead)
            if not has_more:
                return

            if change_sign:
                if DEBUG:
                    print("Changing sign.")
                pi[0] = -pi[0]
            yield pi

    return gen_all


def main():
    def compare(x, y):
        M = {(1, 3), (2, 4)}
        if (x, y) in M:
            return LESS
        if (y, x) in M:
            return GREATER
        return INCOMP

    def visit(S, pi):
        d = ["", "1", "a", "2", "b"]
        s = ("+" if pi[0] > 0 else "-") + ''.join(d[x] for x in pi[1:])
        print(s)
        if s in S:
            print("DUPLICATE - something went wrong!")

    gen = setup(4, compare)
    S = set()
    for pi in gen():
        S.add(tuple(pi))
        visit(S, pi)
    print(len(S))


if __name__ == '__main__':
    main()
