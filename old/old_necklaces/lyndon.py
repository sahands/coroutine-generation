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


def debruijn_cycle(n, k):
    a = setup(n)
    primes = []
    s = []
    ps = []
    for a, p in preprimes(a, k, 1, 1):
        if n % p == 0:
            primes.append(a[:p])
            s.extend(a[:p])
            ps.append(p)
    return primes, s, ps


def test_preprimes(n):
    c = 0
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


def main():
    test_preprimes(5)

if __name__ == '__main__':
    main()
