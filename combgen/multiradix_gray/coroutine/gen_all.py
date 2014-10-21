from .setup import setup


def gen_all(M):
    a, lead = setup(M)
    yield a
    while next(lead):
        yield a
