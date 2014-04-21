from __future__ import print_function


def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


# Usage:
f = fib()  # Create a new "instance" of the generator coroutine
print(next(f))  # Prints 1
print(next(f))  # Prints 1
print(next(f))  # Prints 2
print(next(f))  # Prints 3
print(next(f))  # Prints 5
