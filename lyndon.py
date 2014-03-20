__author__ = "Sahand Saba"


def preprimes(a, k, t, p):
    n = len(a) - 1

    def gen(t, p):
        if t > n:
            yield a[1:], p
        else:
            x = a[t] = a[t - p]
            yield from gen(t + 1, p)
            for j in range(x + 1, k):
                a[t] = j
                yield from gen(t + 1,  t)

    return gen(t, p)


def setup(n):
    a = [0] * (n + 1)
    a[2] = 1
    return a


if __name__ == '__main__':
    c = 0
    n = 4
    a = setup(n)
    for a, p in preprimes(a, 2, 1, 1):
        print(''.join(str(x) for x in a), p, end='')
        c += 1
        if p == n:
            print(" - Lyndon", end='')
        if n % p == 0:
            print(" - Necklace", end='')
        print(end='\n')
    print('Count =', c)
