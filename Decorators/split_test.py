#!/usr/bin/env python3

import functools
import random


def split_test(percent, alt_func):
    """
    Send a percentage of traffic to a nother function
    :param percent: (int) Percentage of calls to route to new_func (0-100).
    :param alt_func: (callable) The alternate function to use.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if random.randint(0, 100) <= percent:
                # Route x% to new function
                return alt_func(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def bar():
    return f'Bar = {random.randint(0, 100):03d}'


@split_test(percent=10, alt_func=bar)
def foo():
    return f'Foo = {random.randint(0, 100):03d}'


def main():
    for _ in range(20):
        print(foo())


if __name__ == '__main__':
    main()
