from combgen.common import cosymsum, coproduct
from .local import chain_poset_ideals_local as X


def setup(n, E):
    a = [0] * n
    Y = []
    k = 0
    for j in E:
        Z = [X(a, i) for i in range(j, k - 1, -1)]
        Y.append(cosymsum(*Z))
        k = j + 1
    lead = coproduct(*Y)
    return a, lead
