#!/usr/bin/env python3

import atexit
import functools
import logging
import random


def counter():
    """
    Count function calls and print ending debug
    :return: function results
    """

    # Track counts
    call_counts = 0
    function = 'unset'

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_counts, function
            call_counts += 1
            function = func.__name__
            return func(*args, **kwargs)

        return wrapper

    # Print function call counts at the end of the program
    @atexit.register
    def print_counts():
        logging.debug(f'{function} Function Call Counts: {call_counts:03d} times')

    return decorator


@counter()
def foo():
    return f'Foo = {random.randint(0, 100):03d}'


@counter()
def bar():
    return f'Bar = {random.randint(0, 100):03d}'


def main():
    for _ in range(20):
        if random.choice((True, False)):
            logging.info(foo())
        else:
            logging.info(bar())


if __name__ == '__main__':
    logging.basicConfig(format='[{asctime}] [{levelname:7}] {message}', level=logging.DEBUG, style='{')
    main()
