def coroutine():
    x = yield "Ready for x"  # Yield "Ready for x", then wait to be passed x
    print(x)


def main():
    c = coroutine()
    value = next(c)
    print(value)  # Prints "Ready for x"
    c.send("Here is x")  # Prints "Here is x", and raises StopIteration

main()
