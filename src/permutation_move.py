from permutation_transpose import transpose

# Movement directions
RIGHT = 1
LEFT = -1

def move(pi, inv, x, d):
    """
    Move x in permutation pi in the direction given by d (+1 or -1,
    corresponding to right and left), while maintaining inv as pi's inverse.
    """
    transpose(pi, inv, x, pi[inv[x] + d])
