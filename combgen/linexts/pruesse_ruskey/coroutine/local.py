from combgen.helpers.permutations import move, LEFT, RIGHT

SWITCH_SIGN = -1  # Signals change of sign in a-b path


def pruesse_ruskey_local(poset, pi, inv, a, b):
    def extended_poset(x, y):  # Extend poset so that a < b
        return (x, y) == (a, b) or poset(x, y)

    while True:
        mra = mrb = 0
        typical = False
        while move(pi, inv, b, RIGHT, extended_poset):
            mrb += 1
            yield True
            mra = 0
            while move(pi, inv, a, RIGHT, extended_poset):
                typical = True
                mra += 1
                yield True
            if typical:
                yield SWITCH_SIGN
                mla = mra + (-1 if mrb % 2 else 1)  # a left moves
                for __ in range(mla):
                    move(pi, inv, a, LEFT)
                    yield True
        if mra > 0 and mrb % 2 == 1:
            move(pi, inv, a, LEFT)
            yield True
        else:
            yield SWITCH_SIGN
        for __ in range(mrb):
            move(pi, inv, b, LEFT)
            yield True
        yield False
