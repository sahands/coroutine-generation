from combgen.helpers.permutations import move, LEFT, RIGHT


MOVED       =  1  # Local coroutine signalling successful transition
DONE        =  0  # Local coroutine is done and will start over next call
SWITCH_SIGN = -1  # Local coroutine signalling change of sign


def can_move_right(n, poset, pi, inv, x):
    i = inv[x]
    if i >= n:
        return False
    right = pi[i + 1]
    return not poset(x, right)


def local(n, poset, pi, inv, a, b):
    # local(a, b) is a coroutine responsible for traversing the
    # Hamiltonian cycle for the 2B-poset in which a is before b, followed
    # immediately by the cycle in which b is before a.

    def extended_poset(x, y):  # Make sure a < b
        return (x, y) == (a, b) or poset(x, y)

    while True:
        mra = mrb = 0
        # If b can not move to the right then we just move a to the right
        # as far as we can.
        if not can_move_right(n, extended_poset, pi, inv, b):
            while can_move_right(n, extended_poset, pi, inv, a):
                move(pi, inv, a, RIGHT)
                mra += 1
                yield MOVED
            yield SWITCH_SIGN
            for __ in range(mra):
                move(pi, inv, a, LEFT)
                yield MOVED
            yield DONE
            continue

        # Otherwise, let's start traversing the path:
        while can_move_right(n, extended_poset, pi, inv, b):
            move(pi, inv, b, RIGHT)
            mrb += 1
            yield MOVED
            while can_move_right(n, extended_poset, pi, inv, a):
                move(pi, inv, a, RIGHT)
                mra += 1
                yield MOVED
            if mra > 0:
                yield SWITCH_SIGN
                if mrb % 2 == 1:
                    mla = mra - 1
                else:
                    mla = mra + 1
                for __ in range(mla):
                    move(pi, inv, a, LEFT)
                    yield MOVED
        if mra > 0 and mrb % 2 == 1:
            move(pi, inv, a, LEFT)
            yield MOVED
        else:
            yield SWITCH_SIGN
        for __ in range(mrb):
            move(pi, inv, b, LEFT)
            yield MOVED
        yield DONE
