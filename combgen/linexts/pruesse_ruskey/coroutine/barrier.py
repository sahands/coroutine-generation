from .local import DONE, SWITCH_SIGN


def pruesse_ruskey_barrier():
    # Just switches the sign continuously.
    while True:
        yield SWITCH_SIGN
        yield DONE
