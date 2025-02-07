#!/usr/bin/env python3


import functools
import hashlib
import logging
import random
import string
import time
import tracemalloc


def profile(func):
    """
    Profile cpu and memory for a function
    :return: function results
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()  # Start memory tracking
        cpu_start = time.process_time()  # CPU time (ignores sleep)

        result = func(*args, **kwargs)  # Execute function

        cpu_end = time.process_time()
        current_mem, peak_mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mem_kb = peak_mem / 1024  # Convert to KB
        peak_mem_mb = peak_mem_kb / 1024  # Convert to MB

        logging.debug(f'Function {func.__name__}:')
        logging.debug(f'\tCPU Time: {cpu_end - cpu_start:.6f} sec')
        logging.debug(f'\tPeak Memory: {peak_mem_kb:.2f} KB ({peak_mem_mb:.2f} MB)')

        return result

    return wrapper


def main():
    for size in range(3, 9):
        # Perform a more intense function
        large_text = ''.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(10 ** size))
        logging.info(hash_large_string(large_text))


@profile
def hash_large_string(text):
    logging.info(f'Hashing {len(text)} characters...')
    return hashlib.sha256(text.encode()).hexdigest()


if __name__ == '__main__':
    logging.basicConfig(format='[{asctime}] [{levelname:7}] {message}', level=logging.DEBUG, style='{')
    main()
