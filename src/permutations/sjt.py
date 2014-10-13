from time import sleep
from sjt_coroutine import permutations as sjtc
from sjt_coroutine import setup
from sjt_recursive import permutations as sjtr
from log_time import log_execution_time


def cyclic_test(n):
    pi, lead = setup(n)
    c = 0
    while True:
        print(''.join(str(x) for x in pi[1:-1]))
        c += 1
        if not next(lead):
            print('-------')
            print(c)
            print('-------')
            sleep(1)
            c = 0


@log_execution_time
def test_generator(gen):
    for __ in gen(10):
        pass


def main():
    print('Testing coroutine-based algorithm:')
    test_generator(sjtc)
    print('Testing recursive algorithm:')
    test_generator(sjtr)
    print('\n'.join(''.join(str(x) for x in pi) for pi in sjtc(1)))
    print('\n'.join(''.join(str(x) for x in pi) for pi in sjtc(2)))
    print('\n'.join(''.join(str(x) for x in pi) for pi in sjtc(3)))
    print('\n'.join(''.join(str(x) for x in pi) for pi in sjtc(4)))
    cyclic_test(3)


if __name__ == '__main__':
    main()
