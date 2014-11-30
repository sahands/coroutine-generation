from .local import SWITCH_SIGN


def pruesse_ruskey_barrier():
    while True:
        yield SWITCH_SIGN
        yield False
