#!/usr/bin/env python3
"""
Script:	lun_10.py
Date:	2021-12-28

Platform: macOS/Windows/Linux

Description:
AKA Mod 10 or just Luhn algorithm.

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
    
    All outputs removed
    """

import argparse
import re


def main():
    # Split numbers into an array
    numbers = [int(number) for number in re.findall(r'[0-9]', ''.join(options.number))]

    if options.check:
        check_sum = numbers[-1]
        numbers = numbers[:-1]

    # Sum the single digits
    even_sum = sum(numbers[-2::-2])

    # Sum the digits that are to be doubled
    odd_sum = sum([int(char) for number in numbers[::-2] for char in str(number * 2)])

    # Sum the number and mod 10
    luhn_sum = (10 - (even_sum + odd_sum)) % 10

    # Perform the check
    return luhn_sum != check_sum if options.check else luhn_sum


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__description__)
    """
    Card number
    """
    parser.add_argument('number', metavar='Number', nargs=argparse.ONE_OR_MORE, help='number pattern')

    """
    Options
    """
    parser.add_argument('-c', '--check', default=False,
                        action='store_true', dest='check',
                        help='perform a check on the number and return 0 on success')

    options = parser.parse_args()

    exit(main())
