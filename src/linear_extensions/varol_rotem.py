def exts(n, M):
    A = range(n + 1)
    inv = A[:]
    yield A[:-1]

    i = 0
    while i < n - 1:
        k = inv[i]
        j = A[k + 1]  # Next item
        if M(i, j):
            # Can not move j to the left, do a cyclical shift to the right
            for l in range(k, i, -1):
                t = A[l - 1]
                inv[t] += 1
                A[l] = t
            inv[i] = A[i] = i
            i += 1
        else:
            A[k], A[k + 1] = j, i
            inv[j] = k
            inv[i] = k + 1
            i = 0
            yield A[:-1]


n = 5

def M(a, b):
    if b == n:
        return True
    if b == 2:
        return a in [0, 1]
    if b == 4:
        return a in [3]
    return False

c = 0
for A in exts(5, lambda a, b: b == n):
    print ''.join(str(x) for x in A)
    c += 1

print c
