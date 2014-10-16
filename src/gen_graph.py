from itertools import islice


def n_grams(a, n):
    z = (islice(a, i, None) for i in range(n))
    return zip(*z)


def generate_adjacency_matrix(alg, neighbour, to_str, *args, **kwargs):
    V = [a[:] for a in alg(*args, **kwargs)]
    lines = []
    for i, v in enumerate(V):
        # This is quite inefficient but it's fine for smaller graphs, which is
        # all we need
        line = ', '.join('1' if neighbour(v, u) else '0' for u in V)
        lines.append(line)

    print('\n'.join(lines))


def generate_pgf_gray_graph(alg, neighbour, to_str, *args, **kwargs):
    V = [a[:] for a in alg(*args, **kwargs)]
    lines = []
    for i, v in enumerate(V):
        # This is quite inefficient but it's fine for smaller graphs, which is
        # all we need
        neighbours = (u for u in V if neighbour(v, u) and abs(V.index(u) - V.index(v)) != 1)
        connections = ', '.join(to_str(u) for u in neighbours)
        line = '{v} -- {{{connections}}};'.format(v=to_str(v), connections=connections)
        lines.append(line)

    for v, u in n_grams(V, 2):
        line = '{v} -> [line width=0.8mm] {{{u}}};'.format(v=to_str(v), u=to_str(u))
        lines.append(line)

    print('\n'.join(lines))
