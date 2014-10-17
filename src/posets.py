def zig_zag(n):
    """
    Returns a function representing the zig zag poset (AKA fence poset)
    for numbers 1 to n, with 1 ... ceil(n/2) on the bottom and
    ceil(n/2) + 1 ... n on the top.
    Example: n = 4
      3  4
     / \/
    1  2
    Example: n = 5
      4  5
     / \/ \
    1  2   3
    """
    k, odd = divmod(n, 2)

    def zig_zag_poset(a, b):
        if a == 1:
            return b == k + 1 + odd
        if a == k + odd:
            return b == n
        if a > k + odd:
            return False
        return b in (a + k - 1 + odd, a + k + odd)

    return zig_zag_poset


def add_min_max(poset, minimum, maximum):
    def poset_with_min_max(a, b):
        if a == minimum or b == maximum:
            return True
        return poset(a, b)

    return poset_with_min_max
