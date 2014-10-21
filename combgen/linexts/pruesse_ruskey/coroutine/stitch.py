from combgen.helpers.permutations import transpose
from .local import local, MOVED, DONE, SWITCH_SIGN


def pruesse_ruskey_stitch(n, poset, pi, inv, a, b, Y):
    u = local(n, poset, pi, inv, a, b)
    w = local(n, poset, pi, inv, b, a)
    while True:
        for result in u:
            if result == DONE:
                break
            yield result

        for result in Y:
            if result == DONE:
                break
            if result == SWITCH_SIGN:
                transpose(pi, inv, a, b)
                u, w = w, u
                a, b = b, a
            yield MOVED
            for result in u:
                if result == DONE:
                    break
                yield result
        yield DONE
