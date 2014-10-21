def prod(A):
    """Returns the product of numbers given by an iterator."""
    p = 1
    for a in A:
        p *= a
    return p


def number_to_multiradix(M, x, a):
    for i in range(len(M)):
        x, a[-i - 1] = divmod(x, M[-i - 1])
    return a


def gen_all(M):
    a = [0] * len(M)
    last = prod(M)
    for x in range(last):
        yield number_to_multiradix(M, x, a)
