import combgen.multiradix_lex.coroutine
import combgen.multiradix_lex.counting
import combgen.multiradix_lex.iterative
import combgen.multiradix_lex.product
import combgen.multiradix_lex.recursive
from combgen.utils import log_execution_time


@log_execution_time
def test_generator(generator):
    M = [10] * 6
    for a in generator(M):
        pass


def basic_test(generator):
    M = [3, 2, 3]
    for a in generator(M):
        print(''.join(str(x) for x in a))


def run_tests():
    for generator in [combgen.multiradix_lex.counting.gen_all,
                      combgen.multiradix_lex.coroutine.gen_all,
                      combgen.multiradix_lex.product.gen_all,
                      combgen.multiradix_lex.iterative.gen_all,
                      combgen.multiradix_lex.recursive.gen_all]:
        print('Testing {}.{}:'.format(generator.__module__,
                                      generator.__name__))
        test_generator(generator)
        print()


if __name__ == '__main__':
    print('\n'.join(''.join(str(x) for x in a) for a in combgen.multiradix_lex.coroutine.gen_all([3, 2, 3])))
    # run_tests()
