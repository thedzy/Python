#!/usr/bin/env python3

import functools
import logging
import random


class Interupt():
    """
    Exit on

    """
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyboardInterrupt:
                print()
                logging.info('User interrupted')

        return wrapper


@Interupt()
def main():
    random_number, iterator, moderator = 0, 0, 999999
    while True:
        iterator += 1
        random_number = random.randint(0, 100000000)
        if iterator % moderator == 0:
            logging.info(f'Random number {random_number*1000000:20,d}')


if __name__ == '__main__':
    logging.basicConfig(format='[{asctime}] [{levelname:7}] {message}', level=logging.INFO, style='{')
    main()
