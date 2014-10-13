from multiradix_coroutine import multiradix_coroutine
from multiradix_counting import multiradix_counting
from multiradix_iterative import multiradix_iterative
from multiradix_product import multiradix_product
from multiradix_recursive import multiradix_recursive
from log_time import log_execution_time


@log_execution_time
def test_generator(generator):
    M = [10] * 7
    for a in generator(M):
        pass


def basic_test(generator):
    M = [3, 2, 3]
    for a in generator(M):
        print(''.join(str(x) for x in a))


def run_tests():
    for generator in [multiradix_product,
                      multiradix_counting,
                      multiradix_recursive,
                      multiradix_iterative,
                      multiradix_coroutine]:
        print('Testing {}:'.format(generator.__name__))
        test_generator(generator)
        print()


if __name__ == '__main__':
    run_tests()
