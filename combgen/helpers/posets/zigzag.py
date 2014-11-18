def zigzag(n):
    # Example for $n=4$: $1<3>2<4$
    # Example for $n=5$: $1<4>2<5>3$
    k = n // 2 + n % 2  # k = ceil(n/2)

    def poset(a, b):
        if a == 1:
            return b == k + 1
        if n % 2 and a == k:
            return b == n
        if a > k:
            return False
        return b in (a + k - 1, a + k)

    return poset
