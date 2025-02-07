#!/usr/bin/env python3

import functools
import logging
import random
import time


def retry(attempts=3, delay=2, exceptions=(Exception,)):
    """
    Retry a function on failure
    :param attempts: (int) Retry limit
    :param delay: (int) Seconds delay between retries
    :param exceptions: (list)(Exception) Exceptions to handle
    :return: function results
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    logging.warning(f'Attempt {attempt + 1} failed for {func.__name__}: {type(err).__name__}: {err}')
                    time.sleep(delay)
            raise RuntimeError(f'Function {func.__name__} failed after {attempts} attempts')

        return wrapper

    return decorator


@retry(attempts=5, delay=1)
def main():
    logging.info(f'Trying...')
    if random.choice(range(0, 5)) == 0:
        return
    else:
        raise random.choice((ValueError, ZeroDivisionError, IndexError))


@retry(attempts=5, delay=1)
def main2():
    logging.info(f'Trying...')
    if random.choice(range(0, 5)) == 0:
        return
    else:
        raise random.choice((ValueError, ZeroDivisionError, IndexError))


if __name__ == '__main__':
    logging.basicConfig(format='[{asctime}] [{levelname:7}] {message}', level=logging.INFO, style='{')
    try:
        main()
        main2()
        logging.info('Function succeeded')
    except RuntimeError as err:
        logging.error(err)
