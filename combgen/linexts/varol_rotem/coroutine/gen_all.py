from .setup import setup


def gen_all(n, poset):
    lead, pi = setup(n, poset)
    while True:
        yield pi[1:-1]
        if not next(lead):
            return
