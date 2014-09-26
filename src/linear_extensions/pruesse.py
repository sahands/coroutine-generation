LESS = -1
GREATER = 1
INCOMP = 0  # Incomparable


DEBUG = False
DEBUG = True


def setup(n, compare, visit):
    # A[0] will be the sign
    A = list(range(n + 1))
    inv = A[:]
    A[0] = +1
    a = [0, 1, 3]
    b = [0, 2, 4]
    RIGHT = 1
    LEFT = -1

    def can_move_a_right(i):
        # True if a[i] can move to the right
        if inv[a[i]] >= n:
            return False
        right = A[inv[a[i]] + 1]
        return right != b[i] and compare(a[i], right) == INCOMP

    def can_move_b_right(i):
        # True if b[i] can move to the right
        if inv[b[i]] >= n:
            return False
        # if DEBUG:
        #     print("inv[b[{}]] = {}".format(i, inv[b[i]]))
        right = A[inv[b[i]] + 1]
        return compare(b[i], right) == INCOMP
        # return compare(b[i], right) == INCOMP

    def transpose(x, y):
        i = inv[x]
        j = inv[y]
        inv[x], inv[y] = j, i
        A[i], A[j] = A[j], A[i]

    def switch(i):
        if i == 0:
            A[0] = -A[0]
            if DEBUG:
                print("Switching sign to {}".format("+" if A[0] > 0 else "-"))
        else:
            if DEBUG:
                print("Switching {} - {} and {}".format(i, a[i], b[i]))
            transpose(a[i], b[i])
            # Ensure a[i] is to the left of b[i]
            a[i], b[i] = b[i], a[i]
        visit(A)

    def move(x, d):
        if DEBUG:
            print("Moving {} in direction {}.".format(x, d))
        transpose(x, A[inv[x] + d])
        visit(A)

    def gen(i):
        if i == 0:
            return

        if DEBUG:
            print("gen({}):".format(i))

        gen(i - 1)
        mrb = 0
        mla = 0
        typical = False
        while can_move_b_right(i):
            mrb += 1
            move(b[i], RIGHT)
            gen(i - 1)
            mra = 0
            if can_move_a_right(i):
                typical = True
                while True:
                    mra += 1
                    move(a[i], RIGHT)
                    gen(i - 1)
                    if not can_move_a_right(i):
                        break
            if typical:
                switch(i - 1)
                gen(i - 1)
                if mrb % 2 == 1:
                    mla = mra - 1
                else:
                    mla = mra + 1
                for x in range(1, mla + 1):
                    move(a[i], LEFT)
                    gen(i - 1)
        if typical and mrb % 2 == 1:
            move(a[i], LEFT)
        else:
            switch(i - 1)
        gen(i - 1)
        for x in range(1, mrb + 1):
            move(b[i], LEFT)
            gen(i - 1)

        if DEBUG:
            print('-- gen({})'.format(i))

    def gen_all():
        m = len(a) - 1
        visit(A)
        gen(m)
        switch(m)
        gen(m)

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
        # s = ("+" if A[0] > 0 else "-") + ''.join(str(x) for x in A[1:])
        s = ("+" if A[0] > 0 else "-") + ' '.join(d[x] for x in A[1:])
        print(s)
        S.append(s)

    gen = setup(4, compare, visit)
    gen()
    print(len(S))


if __name__ == '__main__':
    main()
