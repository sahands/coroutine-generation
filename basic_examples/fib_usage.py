from fib import fib


f = fib()       # Create a new "instance" of the generator coroutine
print(next(f))  # Prints 1
print(next(f))  # Prints 1
print(next(f))  # Prints 2
print(next(f))  # Prints 3
print(next(f))  # Prints 5
print(next(f))  # etc...
