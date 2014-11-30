from combgen.helpers.permutations import transpose
from .local import pruesse_ruskey_local, SWITCH_SIGN


def pruesse_ruskey_product(poset, pi, inv, a, b, Y):
    X_ab = pruesse_ruskey_local(poset, pi, inv, a, b)
    X_ba = pruesse_ruskey_local(poset, pi, inv, b, a)
    while True:
        for result in X_ab:
            if not result:
                break
            yield result

        for result in Y:
            if not result:
                break
            if result is SWITCH_SIGN:
                transpose(pi, inv, a, b)
                X_ab, X_ba = X_ba, X_ab
                a, b = b, a
            yield True
            for result in X_ab:
                if not result:
                    break
                yield result
        yield False
