def zigzag(n):
    # Returns a function representing the zig zag poset (i.e. fence poset) for
    # numbers $1$ to $n$, with $1,\ldots,\lceil\frac{n}{2}\rceil$ on the bottom
    # and $\lceil\frac{n}{2}\rceil+1,\ldots,n$ on the top.
    # Example for $n=4$: $1<3>2<4$
    # Example for $n=5$: $1<4>2<5>3$
    k, odd = divmod(n, 2)

    def poset(a, b):
        if a == 1:
            return b == k + 1 + odd
        if a == k + odd:
            return b == n
        if a > k + odd:
            return False
        return b in (a + k - 1 + odd, a + k + odd)

    return poset
