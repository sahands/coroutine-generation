def can_move(n, poset, pi, inv, x, direction):
    i = inv[x]
    if 1 <= (i + direction) <= n:
        right = pi[i + 1]
        return not poset(x, right)
    return False
