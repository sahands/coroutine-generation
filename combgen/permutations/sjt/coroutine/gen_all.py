from .setup import setup


def gen_all(n):
    pi, lead = setup(n)
    yield pi[1:-1]
    while next(lead):
        yield pi[1:-1]
