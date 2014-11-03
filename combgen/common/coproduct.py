from combgen.common import comultiply


def coproduct(*Xs):
    iterator = iter(Xs)
    lead = next(iterator)
    for X in iterator:
        lead = comultiply(lead, X)
    return lead
