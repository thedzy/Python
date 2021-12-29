#!/usr/bin/env python3
"""
Script:	lun_10.py
Date:	2021-12-28

Platform: macOS/Windows/Linux

Description:
AKA Mod 10 or just Luhn10.

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2021, thedzy'
__license__ = 'GPL'
__version__ = '2.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'
__description__ = """
    Calculate or validate a luhn10 number
    Return checksum on calculate
    Return 0 on successful check
    """

import argparse
import logging
import re


def main():
    logging.basicConfig(format='{message}', level=options.debug, style='{')

    # Split numbers into an array
    numbers = [int(number) for number in re.findall(r'[0-9]', ''.join(options.number))]

    if options.check:
        logging.info('Performing check')
        check_sum = numbers[-1]
        numbers = numbers[:-1]
        logging.debug(f'Checksum {check_sum}')

    logging.debug(f'Numbers: {numbers}')

    # Determine parity
    even = len(numbers) % 2
    odd = (even + 1) % 2

    # Sum the single digits
    logging.debug(f'Single Sums: {numbers[even::2]}')
    even_sum = sum(numbers[even::2])
    logging.debug(f'Summed: {even_sum}')

    # Sum the digits that are to be doubled
    logging.debug(f'Double Sums: {numbers[odd::2]}')
    logging.debug(f'Double Sums: {[int(char) for number in numbers[odd::2] for char in str(number * 2)]}')
    odd_sum = sum([int(char) for number in numbers[odd::2] for char in str(number * 2)])
    logging.debug(f'Summed: {odd_sum}')

    # Sum the number and mod 10
    logging.debug(f'Total Sum: {sum([even_sum, odd_sum])}')
    luhn_sum = (10 - (even_sum + odd_sum)) % 10
    logging.debug(f'Check sum: 10 - {even_sum + odd_sum} % 10 = {luhn_sum}')


    # Perform the check
    if options.check:
        if luhn_sum == check_sum:
            logging.info('Passed')
            return 0
        else:
            logging.info('Failed')
            return 1
    else:
        numbers.append(luhn_sum)
        logging.info(group_numbers(numbers))
        return luhn_sum


def group_numbers(numbers, dividers=[7, 5, 4, 3, 2]):
    """
    Group numbers into the largest divider
    :param numbers: (list)(int) Numbers
    :param dividers: (list)(int) Numbers to try and group into
    :return: (str) Grouped numbers
    """
    length = len(numbers)
    dividers.append(length)

    # Find the first group to match the size
    for divider in dividers:
        if length % divider == 0:
            size = divider
            break

    # Group numbers
    groups = []
    for index in range(0, length, size):
        section_set = [str(number) for number in numbers[index:index + size]]
        groups.append(''.join(section_set))

    return ' '.join(groups)


if __name__ == '__main__':

    def parser_formatter(format_class, **kwargs):
        """
        Use a raw parser to use line breaks, etc
        :param format_class: (class) formatting class
        :param kwargs: (dict) kwargs for class
        :return: (class) formatting class
        """
        try:
            return lambda prog: format_class(prog, **kwargs)
        except TypeError:
            return format_class


    parser = argparse.ArgumentParser(description='lun_10.py',
                                     formatter_class=parser_formatter(argparse.RawTextHelpFormatter,
                                                                      indent_increment=4, max_help_position=12,
                                                                      width=160))
    """
    Card number
    """
    parser.add_argument('number', metavar='Number', nargs=argparse.ONE_OR_MORE,
                        help='Number pattern')

    """
    Options
    """
    parser.add_argument('--check',
                        action='store_true', dest='check', default=False,
                        help='perform a check on the number and return 0 on success')

    parser.add_argument('--debug', const=10, default=20,
                        action='store_const', dest='debug',
                        help=argparse.SUPPRESS)

    options = parser.parse_args()

    exit(main())
