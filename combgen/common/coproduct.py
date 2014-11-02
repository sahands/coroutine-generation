from combgen.common import comultiply


def coproduct(*Xs):
    reversed_iterator = reversed(Xs)  # Stitch in reverse order
    lead = next(reversed_iterator)  # Start with the last coroutine
    for X in reversed_iterator:
        lead = comultiply(X, lead)
    return lead
