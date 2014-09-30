from time import sleep
from itertools import cycle
from varol_rotem import zig_zag


def nobody():
    while True:
        yield False


def cyclic_shift(A, inv, start, end, direction):
    r = range(start + 1, end + 1) if direction == 1 else range(end, start, -1)
    for k in r:
        t = A[k + direction]
        inv[t] -= direction
        A[k] = t
    inv[start] = A[start] = start


d = -1


def troll(i, M, A, inv, trolls):
    while True:
        k = inv[i]
        j = A[k - d]  # j is the next item
        # print(i, j, M(i, j))
        if M(i, j):
            # print('A', i, k)
            # Can not move j to the left, do cyclic shift
            cyclic_shift(A, inv, i, k, d)
            yield next(trolls[i - d])
        else:
            # print('B', i)
            A[k], A[k - d] = j, i
            inv[j], inv[i] = k, k + 1
            yield True


def setup(n, M):
    A = list(range(n + 2))
    inv = A[:]
    trolls = [nobody()]
    trolls.extend(troll(i, M, A, inv, trolls) for i in range(1, n + 1))
    trolls.append(nobody())
    return cycle([trolls[1], trolls[n]]), A


def test(n, M=None):
    global d
    # M = M or (lambda a, b: b == n + 1)
    z = zig_zag(n)
    M = lambda a, b: z(a - 1, b - 1)
    c = 0
    leaders, A = setup(n, M)
    lead = next(leaders)
    while True:
        c += 1
        print(c, ''.join(str(x) for x in A[1:-1]))
        if not next(lead):
            print('-----')
            # break  # For now, the repeat in oppositve order does not work
            sleep(1)
            lead = next(leaders)
            d = -d


def main():
    # test(3)
    test(4)
    # test(5)
    # test(6)
    # test(7)
    exit()

    n = 5

    def M(a, b):
        if b == n:
            return True
        if a == 0:
            return False
        if b == 2:
            return a in [0, 1]
        if b == 4:
            return a in [3]
        return False


if __name__ == '__main__':
    main()
