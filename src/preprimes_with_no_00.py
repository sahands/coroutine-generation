from lyndon import preprimes


def print_primes_with_no_00(n, count_only=False):
    a = [0] * (n + 1)
    a[2] = 1
    c = 0
    for a, p in preprimes(a, 2, 3, 2):
        if p == n:
            c += 1
            if not count_only:
                print(''.join(str(x) for x in a), p)
    print('Count =', c)


if __name__ == '__main__':
    for n in range(2, 21):
        print_primes_with_no_00(n)
