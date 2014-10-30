DONE = False
MOVED = True


def while_not_done(coroutine):
    while True:
        r = next(coroutine)
        if r == DONE:
            break
        yield r


def bridging_stitch(X, Y):
    # Produce pattern (X Y |)*
    while True:
        yield from while_not_done(X)
        yield from while_not_done(Y)
        yield DONE


# Probabyl not an accurate, I don't really know what "hemstiching" is!
def hem_stitch(X, Y):
    # Produce pattern (X Y | Y X)*
    while True:
        yield from while_not_done(bridging_stitch(X, Y))
        yield DONE
        yield from while_not_done(bridging_stitch(Y, X))
        yield DONE


def blind_stitch(X, Y):
    # Produce pattern (Y x_1 Y x_2 Y x_3 Y ... Y x_n)*
    while True:
        yield from while_not_done(Y)
        yield next(X)


def X(a, i):
    while True:
        a[i] = 1 - a[0]
        yield True
        yield False


def stitch_coroutines(coroutine_list, stitching_pattern):
    reversed_iterator = reversed(coroutine_list)  # Stitch in reverse order
    lead = next(reversed_iterator)  # Start with the last coroutine
    for X in reversed_iterator:
        lead = stitching_pattern(X, lead)
    return lead


def main():
    n = 5
    a = [0] * n
    lead = blind_stitch(hem_stitch(X(a, 1), X(a, 0)),
                       hem_stitch(X(a, 4), hem_stitch(X(a, 3), X(a, 2))))

    k = 0
    c = 0
    while True:
        k += 1
        print(''.join(str(x) for x in a))
        if not next(lead):
            print('--', k, '--')
            k = 0
            c += 1
            if c > 2:
                break


if __name__ == '__main__':
    main()
