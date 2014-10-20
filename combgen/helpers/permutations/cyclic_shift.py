def left_cyclic_shift(pi, inv, i, j):
    x = pi[i]
    for k in range(i, j):
        t = pi[k + 1]
        inv[t] -= 1
        pi[k] = t
    inv[x] = j
    pi[j] = x
