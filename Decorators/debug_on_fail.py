#!/usr/bin/env python3

import functools
import logging
import pdb
import random


def debug_on_fail(func):
    """
    If active, enters the debugger when an exception occurs.

    :param active: (bool) If False, it will log the error instead of debugging.
    """

    # Flag to deactivate in teh event there is an instance that is not removed
    active = True

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f'Error in {func.__name__}: {e}')
            if active:  # Only enter debugger if active=True
                pdb.post_mortem()
            else:
                raise  # Re-raise exception if debugging is disabled

    return wrapper


@debug_on_fail
def foo():
    if random.randint(0, 10) == 0:
        return f'Foo = {random.randint(0, 100):03d}'
    else:
        raise ValueError


def main():
    for _ in range(20):
        print(foo())


if __name__ == '__main__':
    logging.basicConfig(format='[{asctime}] [{levelname:7}] {message}', level=logging.DEBUG, style='{')
    main()
