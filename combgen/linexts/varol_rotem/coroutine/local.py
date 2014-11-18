from combgen.helpers.permutations import move, LEFT, left_cyclic_shift


def varol_rotem_local(poset, pi, inv, x):
    # Move i to the left while maintaining pi as a linear extension of poset.
    # When i can no longer move to the left, do a cyclic shift to put i back to
    # its starting position.
    while True:
        while move(pi, inv, x, LEFT, poset):
            yield True
        left_cyclic_shift(pi, inv, inv[x], x)
        yield False
