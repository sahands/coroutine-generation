from __future__ import print_function


def add_func(a, b):
    return a + b


def add_coroutine(a, b):
    yield a + b


# Usage:
x = add_func(1, 2)
print(x)

# Equivalent to:
adder = add_coroutine(1, 2)
x = next(adder)
print(x)

# Further calls such as the following to adder will result in a StopIteration
# being raised.
x = next(adder)
