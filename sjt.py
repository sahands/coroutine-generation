from time import sleep

__author__ = "Sahand Saba"


def nobody():
    while True:
        yield False


# The term "troll" is taken from Knuth's choice of word
def sjt(pi, inv, i, trolls):
    d = -1  # Directoin. -1 is descending, +1 is ascending.
    while True:
        j = inv[i]  # j is the position of the current "troll"
        if pi[j] < pi[j + d]:
            d = -d
            yield next(trolls[i - 1])
        else:
            pi[j], pi[j + d] = pi[j + d], pi[j]
            inv[i] += d
            inv[pi[j]] -= d
            yield True


def setup(n):
    # Pad pi with n + 2, so that pi[i] will always be < the two ends.
    pi = [n + 2] + [i for i in range(1, n + 1)] + [n + 2]
    inv = pi[:-1]
    # nobody simply continuously yields False. By adding a "nobody" generator
    # at both ends of trolls, False is autmatically yieded by sjt when needed.
    trolls = [nobody()]
    trolls.extend(sjt(pi, inv, i + 1, trolls) for i in range(n))
    trolls += [nobody()]
    # The lead troll will be the item n in the permutation
    lead_troll = trolls[-2]
    return pi, lead_troll


def permutations(n):
    pi, lead_troll = setup(n)
    yield pi[1:-1]
    while next(lead_troll):
        yield pi[1:-1]


def cyclic_test(n):
    pi, lead_troll = setup(n)
    c = 0
    while True:
        print('Output: ', ''.join(str(x) for x in pi[1:-1]))
        c += 1
        if not next(lead_troll):
            print('-------')
            print(c)
            print('-------')
            sleep(1)
            c = 0


if __name__ == '__main__':
    print('\n'.join(''.join(str(x) for x in pi) for pi in permutations(1)))
    print('\n'.join(''.join(str(x) for x in pi) for pi in permutations(2)))
    print('\n'.join(''.join(str(x) for x in pi) for pi in permutations(3)))
    print('\n'.join(''.join(str(x) for x in pi) for pi in permutations(4)))
    cyclic_test(3)
