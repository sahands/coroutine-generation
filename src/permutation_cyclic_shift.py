def left_cyclic_shift(pi, inv, start, end):
    i = pi[start]
    for k in range(start, end):
        t = pi[k + 1]
        inv[t] -= 1
        pi[k] = t
    inv[i] = end
    pi[end] = i
