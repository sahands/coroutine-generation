def multiradix_iterative(M):
    n = len(M)
    a = [0] * n
    while True:
        yield a
        # Find right-most index k such that a[k] < M[k] - 1 by scanning from
        # right to left, and setting everything to zero on the way.
        k = n - 1
        while a[k] == M[k] - 1:
            a[k] = 0
            k -= 1
            if k < 0:
                # Last lexicographic item
                return
        a[k] += 1
