#!/usr/bin/env python3

import logging
import sys


def redirect_print_to_log(func):
    """
    Convert print statments to logging.info
    :param func: (callable) Function
    :return:
    """

    def wrapper(*args, **kwargs):
        class LoggerWriter:
            def write(self, message):
                if message.strip():
                    logging.info(message.strip())

            def flush(self):
                pass  # Compatibility with sys.stdout

        original_stdout = sys.stdout
        sys.stdout = LoggerWriter()
        try:
            return func(*args, **kwargs)
        finally:
            sys.stdout = original_stdout  # Restore original stdout

    return wrapper


def main():
    print('This is a print statements')
    main2()
    main3()


@redirect_print_to_log
def main2():
    print('This is now an info log.')
    print('Another log message.')


def main3():
    print('This is now an NOT log.')
    print('Another print message.')


if __name__ == '__main__':
    logging.basicConfig(format='[{asctime}] [{levelname:7}] {message}', level=logging.INFO, style='{')
    main()
