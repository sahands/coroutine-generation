from time import sleep
from combgen.permutations.sjt.coroutine import setup, gen_all
from combgen.permutations.sjt.recursive import gen_all as recursive_gen_all
from combgen.utils import log_execution_time


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
    # cyclic_test(3)
    print('Testing coroutine-based algorithm:')
    test_generator(gen_all)
    print('Testing recursive algorithm:')
    test_generator(recursive_gen_all)
    print('\n'.join(''.join(str(x) for x in pi) for pi in gen_all(1)))
    print('\n'.join(''.join(str(x) for x in pi) for pi in gen_all(2)))
    print('\n'.join(''.join(str(x) for x in pi) for pi in gen_all(3)))
    print('\n'.join(''.join(str(x) for x in pi) for pi in gen_all(4)))
    cyclic_test(3)


if __name__ == '__main__':
    main()
