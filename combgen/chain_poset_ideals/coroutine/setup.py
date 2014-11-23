from combgen.common import cosymsum, coproduct
from .local import chain_poset_ideals_local as X


def setup(n, E):
    a = [0] * n
    Y = []
    for j in range(len(E) - 1):
        Z = [X(a, i) for i in range(E[j] + 1, E[j + 1] + 1)]
        Y.append(cosymsum(*Z))
    lead = coproduct(*Y)
    return a, lead
