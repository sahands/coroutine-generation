def transpose(pi, inv, x, y):
    """
    Transpose x and y in permutation pi while maintaining inv as pi's
    inverse.
    """
    i = inv[x]
    j = inv[y]
    inv[x], inv[y] = j, i
    pi[i], pi[j] = pi[j], pi[i]
