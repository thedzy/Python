#!/usr/bin/env python3

import functools
import inspect
import logging
import os
import random
import sys
import re


def debug(func):
    """
    Print each line of the function to logging debug
    :param func: (callable) Function
    :return:
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        replace_variable_inline = True  # Print varaible or replace variables in line

        # Print calling function
        logging.debug(f'Calling {func.__name__} with args={args}, kwargs={kwargs}')

        def trace(frame, event, arg):
            # Skip call traces, maybe also return and exceptions
            if event in ('call', 'return'):
                return trace

            # Lets keep statements for only calls within the file
            if os.path.abspath(frame.f_code.co_filename) != os.path.abspath(func.__code__.co_filename):
                return trace

            # Condense message
            code_context = inspect.getframeinfo(frame).code_context
            frame_locals = frame.f_locals
            if code_context:
                line = ' '.join([line.strip() for line in code_context])
                if replace_variable_inline:
                    try:
                        # Find variable names
                        for var in re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', line):
                            # Replace if it's a variable
                            if var in frame_locals:
                                # Update line with value of variable
                                line = line.replace(var, str(frame_locals[var]))
                    except KeyError:
                        pass
                else:
                    line = f'{line} | Variables: {frame_locals}'

                logging.debug(f'[{func.__name__}:{frame.f_lineno}] {line}')
            return trace

        sys.settrace(trace)
        try:
            result = func(*args, **kwargs)
        finally:
            sys.settrace(None)

        logging.debug(f'{func.__name__} returned {result}')
        return result

    return wrapper


@debug
def main(low, high):
    logging.info('Start')
    random_int = random.randint(low, high)
    for exponent in range(random_int):
        logging.info(f'{exponent:02d}: {2 ** exponent}')

    return random_int


if __name__ == '__main__':
    logging.basicConfig(format='[{asctime}] [{levelname:7}] {message}', level=logging.DEBUG, style='{')
    main(3, 10)
