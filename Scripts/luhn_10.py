#!/usr/bin/env python3
"""
Script:	lun_10.py
Date:	2020-08-08	

Platform: macOS/Windows/Linux

Description:
AKA Mod 10 or just Luhn.

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2020, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'

import argparse
import re


def main(number, check, debug):
    # Split numbers into an array
    numbers = re.findall(r'[0-9]', ''.join(number))

    if check:
        original = numbers
        numbers = numbers[:-1]

    # Calculate from right to left
    numbers.reverse()

    if debug:
        print(numbers)

    # Calculate sum of numbers
    luhn_sum = 0
    for index in range(len(numbers)):
        digit = int(numbers[index])
        if bool(index % 2):
            luhn_sum += digit
            if debug:
                print('{} -> {}'.format(numbers[index], digit))
        else:
            luhn_double = digit * 2 if digit * 2 < 10 else digit * 2 - 9
            luhn_sum += luhn_double
            if debug:
                print('{} -> {}'.format(numbers[index], luhn_double))

    if debug:
        print('Sum:     ', luhn_sum)
        print('Sum * 9: ', luhn_sum * 9)

    # Calculate check sum
    luhn_check_sum = (luhn_sum * 9) % 10

    # Restore order
    numbers.reverse()

    # Print final number digit groups
    split_range = 1
    for integer in range(int(len(numbers)/2), 0, -1):
        if (len(numbers) + 1) % integer == 0:
            split_range = integer
            break
    pattern = re.compile('[0-9]{{1,{0}}}'.format(split_range))
    numbers_final = pattern.findall(''.join(numbers) + str(luhn_check_sum))

    print('The number: {} has a check sum of {}'.format(' '.join(numbers), luhn_check_sum))
    print('The full number is:\n{}'.format(' '.join(numbers_final)))

    if check:
        if debug:
            print('Original:  ', ''.join(original), original)
            print('Calculated:', ''.join(numbers_final), numbers_final)
        if ''.join(original) != ''.join(numbers_final):
            print('Invalid')
            return 1
        else:
            print('Valid')

    return 0


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
                        help='Perform a check instead of a calculations')

    parser.add_argument('--debug',
                        action='store_true', dest='debug', default=False,
                        help=argparse.SUPPRESS)

    options = parser.parse_args()

    exit(main(options.number, options.check, options.debug))
