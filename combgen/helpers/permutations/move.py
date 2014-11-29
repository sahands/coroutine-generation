from .transpose import transpose

# Movement directions
LEFT = -1
RIGHT = 1


def move(pi, inv, x, d, poset=None):
    # Move x in permutation pi in the direction given by d, while maintaining
    # inv as pi's inverse.  If a poset is given, x is only moved if pi will
    # continue to be a linear extension of the poset with x moved. True is
    # returned if move is successful.
    if inv[x] + d >= len(pi) or inv[x] + d < 1:
        return False
    y = pi[inv[x] + d]
    if poset and ((d == LEFT and poset(y, x)) or (d == RIGHT and poset(x, y))):
        return False
    transpose(pi, inv, x, pi[inv[x] + d])
    return True
