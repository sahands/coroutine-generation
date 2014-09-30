LESS = -1
GREATER = 1
INCOMP = 0  # Incomparable
RIGHT = 1
LEFT = -1

DEBUG = False
DEBUG = True


def setup(n, compare):
    A = list(range(n + 1))
    inv = A[:]
    A[0] = 1

    def transpose(x, y):
        i = inv[x]
        j = inv[y]
        inv[x], inv[y] = j, i
        A[i], A[j] = A[j], A[i]

    def move(x, d):
        if DEBUG:
            print("Moving {} in direction {}.".format(x, d))
        transpose(x, A[inv[x] + d])

    def can_move_a_right(a, b):
        # True if a[i] can move to the right
        i = inv[a]
        if i >= n:
            return False
        right = A[i + 1]
        return right != b and compare(a, right) == INCOMP

    def can_move_b_right(b):
        # True if b[i] can move to the right
        i = inv[b]
        if i >= n:
            return False
        right = A[i + 1]
        return compare(b, right) == INCOMP

    def gnome():
        """Just switches the sign and yields True, then False, continuously."""
        while True:
            yield True, False

    def nobody():
        while True:
            yield False

    def troll(a, b):
        """
        troll(a, b) is a coroutine responsible for traversing the Hamiltonian
        cycle for the 2B-poset in which a is before b, followed immediately by
        the cycle in which b is before a.
        """
        while True:
            mra = mrb = 0
            # If b can not move to the right then we just change sign and are
            # done
            if not can_move_b_right(b):
                yield True, False

            # Otherwise, let's start traversing the path:
            while can_move_b_right(b):
                move(b, RIGHT)
                mrb += 1
                yield False, True
                while can_move_a_right(a, b):
                    move(a, RIGHT)
                    mra += 1
                    yield False, True
                if mra > 0:
                    yield True, True
                    if mrb % 2 == 1:
                        mla = mra - 1
                    else:
                        mla = mra + 1
                    for __ in range(mla):
                        move(a, LEFT)
                        yield False, True
            if mra > 0 and mrb % 2 == 1:
                move(a, LEFT)
                yield False, True
            else:
                yield True, True
            for __ in range(mrb):
                move(b, LEFT)
                yield False, False

    def glue(a, b, t):
        u = troll(a, b)
        w = troll(b, a)
        for change_sign, has_more in t:
            print(change_sign, has_more)
            if change_sign:
                print("Switch {} and {}".format(a, b))
                transpose(a, b)
                u, w = w, u
            yield False, True
            for u_change_sign, u_has_more in u:
                print("u", u_change_sign, u_has_more)
                yield u_change_sign, has_more or u_has_more
                if not u_has_more:
                    break

    def gen_all():
        # t1 = troll(1, 2, gnome())
        # t2 = troll(3, 4, t1)
        yield A
        # for change_sign, has_more in troll(1, 2):
        # for change_sign, has_more in troll(3, 4):
        for change_sign, has_more in glue(1, 2, glue(3, 4, gnome())):
            if change_sign:
                if DEBUG:
                    print("Changing sign.")
                A[0] = -A[0]
            yield A
            if not has_more:
                break

    return gen_all


def main():
    def compare(x, y):
        M = {(1, 3), (2, 4)}
        if (x, y) in M:
            return LESS
        if (y, x) in M:
            return GREATER
        return INCOMP

    S = []

    def visit(A):
        d = ["", "a1", "b1", "a2", "b2"]
        # d = ["", "1", "2"]
        # s = ("+" if A[0] > 0 else "-") + ''.join(str(x) for x in A[1:])
        s = ("+ " if A[0] > 0 else "- ") + ' '.join(d[x] for x in A[1:])
        print("   " + s)
        S.append(s)

    gen = setup(4, compare)
    for A in gen():
        visit(A)
    print(len(S))


if __name__ == '__main__':
    main()
