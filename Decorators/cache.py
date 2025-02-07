#!/usr/bin/env python3

import functools
import time
import pprint


def cache(expiry=60):
    """
    Cache function results for x seconds
    :param expiry: (int) cache time limit
    :return: function results
    """

    def decorator(func):
        # Data store
        cached_results = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            current_time = time.time()

            # Check if we have a recent cached result
            if key in cached_results:
                timestamp, result = cached_results[key]
                if current_time - timestamp < expiry:
                    # Return cached result if within expiry time
                    return result

            # Perform teh function
            result = func(*args, **kwargs)
            cached_results[key] = (current_time, result)
            return result

        return wrapper

    return decorator


@cache()
def lookup_user(username):
    print(f'Getting {username}...')

    # Do real lookup here
    time.sleep(5)
    return {'username': username, 'age': 20, 'sex': 'male'}


def main():
    # Measure time without cache
    start = time.time()
    details = lookup_user('Bob')
    print(f'1st run took: {time.time() - start:.5f} seconds')
    pprint.pp(details)

    # Measure time with cache
    start = time.time()
    details = lookup_user('Bob')
    print(f'2nd run took: {time.time() - start:.5f} seconds')
    pprint.pp(details)


if __name__ == '__main__':
    main()
