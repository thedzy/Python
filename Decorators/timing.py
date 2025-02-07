#!/usr/bin/env python3

import time
import logging

def timing(func):
    """
    Measure timing of a function for performance anaysis
    :param func: (callable) Function
    :return:
    """

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        logging.debug(f'Function {func.__name__} took {end_time - start_time:.6f} seconds')
        return result

    return wrapper


def main():
    logging.info('Start')
    main2()


@timing
def main2():
    logging.info('Start')
    time.sleep(3)
    logging.info('End')


if __name__ == '__main__':
    logging.basicConfig(format='[{asctime}] [{levelname:7}] {message}', level=logging.DEBUG, style='{')
    main()
