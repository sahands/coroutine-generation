from __future__ import print_function

from time import time
from functools import wraps


def log_execution_time(func):
    """Simple decorator to print execution time of a method."""
    @wraps(func)
    def _func(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        execution_time = time() - start_time
        print('Function {} took {:05.3f} seconds to run.'.format(
              func.__name__, execution_time))

    return _func
