from .setup import setup


def gen_all(n, E):
    a, lead = setup(n, E)
    yield a
    while next(lead):
        yield a
