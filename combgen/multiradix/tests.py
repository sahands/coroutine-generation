from combgen.multiradix import multiradix_coroutine
from combgen.multiradix import multiradix_counting
from combgen.multiradix import multiradix_iterative
from combgen.multiradix import multiradix_product
from combgen.multiradix import multiradix_recursive
from combgen.utils import log_execution_time


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
                      lambda M: multiradix_recursive(M, len(M) - 1),
                      multiradix_iterative,
                      multiradix_coroutine]:
        print('Testing {}:'.format(generator.__name__))
        test_generator(generator)
        print()


if __name__ == '__main__':
    run_tests()
