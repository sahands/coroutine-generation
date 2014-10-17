from permutation_transpose import transpose

# Movement directions
RIGHT = 1
LEFT = -1


def move(pi, inv, x, d, poset=None):
    """
    Move x in permutation pi in the direction given by d (+1 or -1,
    corresponding to right and left), while maintaining inv as pi's inverse.
    If a poset is given, x is only moved if pi will continue to be a linear
    extension of the poset with x moved. True is returned if move is
    successful.
    """
    y = pi[inv[x] + d]
    if poset and poset(y, x):
        return False
    transpose(pi, inv, x, pi[inv[x] + d])
    return True
