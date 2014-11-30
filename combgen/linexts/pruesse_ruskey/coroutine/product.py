from combgen.helpers.permutations import transpose
from .local import pruesse_ruskey_local, SWITCH_SIGN


def pruesse_ruskey_product(poset, pi, inv, X, a, b):
    Y_ab = pruesse_ruskey_local(poset, pi, inv, a, b)
    Y_ba = pruesse_ruskey_local(poset, pi, inv, b, a)
    while True:
        for result in Y_ab:
            if not result:
                break
            yield result

        for result in X:
            if not result:
                break
            if result is SWITCH_SIGN:
                transpose(pi, inv, a, b)
                Y_ab, Y_ba = Y_ba, Y_ab
                a, b = b, a
            yield True
            for result in Y_ab:
                if not result:
                    break
                yield result
        yield False
