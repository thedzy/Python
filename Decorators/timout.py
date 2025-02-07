#!/usr/bin/env python3

import functools
import signal
import time


class TimeoutException(Exception):
    pass


def timeout(seconds=5):
    """
    Timout a function if its taking too long
    :param seconds: (int) timeout in seconds
    :return:
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def handler(signum, frame):
                raise TimeoutException(f'Function {func.__name__} timed out after {seconds} seconds')

            # Set the timeout signal and set the time
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)

            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)

            return result

        return wrapper

    return decorator


def main():
    for time_limit in range(3, 7):
        print(f'Running for {time_limit} seconds')
        timed_function(time_limit)


@timeout(5)
def timed_function(time_limit):
    # Simulating a task
    for time_elapsed in range(time_limit):
        time.sleep(1)
        print(time_elapsed + 1, end='...')
    print('Finished')


if __name__ == '__main__':
    try:
        main()
    except TimeoutException as err:
        print(err)
