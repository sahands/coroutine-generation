def nobody():
    while True:
        yield False


def setup(n, M):
    A = list(range(n + 1))
    inv = A[:]
    trolls = []

    def troll(i):
        while True:
            d = 1
            k = inv[i]
            j = A[k + d]
            if M(i, j):
                # Can not move j to the left, do cyclic shift
                for l in range(k, i, -1):
                    t = A[l - 1]
                    inv[t] += 1
                    A[l] = t
                inv[i] = A[i] = i
                yield next(trolls[i + 1])
            else:
                A[k], A[k + 1] = j, i
                inv[j], inv[i] = k, k + 1
                yield True

    trolls.extend(troll(i) for i in range(n))
    trolls.append(nobody())
    return trolls[0], A


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
# lead, A = setup(n, M)
lead, A = setup(n, lambda a, b: b == n)
while True:
    c += 1
    print c, ''.join(str(x) for x in A[:-1])
    if not next(lead):
        break
    raw_input()

print c
