#!/usr/bin/env python3

import argparse
from pathlib import Path


def main():
    print_out_format = '{:15s} {:12}: {}'

    title('Paths')
    print(print_out_format.format('path', '-p', options.path))
    value = options.file_in.name if options.file_in else None
    print(print_out_format.format('file_in', '-r', value))
    value = options.file_out.name if options.file_out else None
    print(print_out_format.format('file_out', '-w', value))

    title('Numbers')
    print(print_out_format.format('integer', '-i1', options.integer))
    print(print_out_format.format('integer_range', '-i2', options.integer_range))
    print(print_out_format.format('float', '-f1', options.float))
    print(print_out_format.format('float_range', '-f2', options.float_range))

    title('Strings')
    print(print_out_format.format('string', '-s', options.string))

    title('Multiple arguments')
    print(print_out_format.format('nargs_two', '-n2', options.nargs_two))
    print(print_out_format.format('nargs_one_plus', '-n2', options.nargs_one_plus))
    print(print_out_format.format('nargs_zero_plus', '-n3', options.nargs_zero_plus))

    title('Required')
    print(print_out_format.format('required', '-e', options.required))

    title('Mutual exclusive')
    print(print_out_format.format('bool', '--yes --no', options.bool))

    title('Hidden')
    print(print_out_format.format('debug', '--debug', options.debug))

    title('Positional arguments')
    print(print_out_format.format('positional', '', options.positional))


def title(text='', width=40):
    print('\n')
    print('-' * width)
    print(text)
    print('-' * width)


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


    def directory(path):
        """
        Validate directory path
        :param path: (string) Path
        :return: Path, exception
        """
        if Path(path).is_dir():
            return path
        else:
            argparse.ArgumentError('{} does not appear to be a valid directory'.format(path))


    def number_range(low, high, obj_type=int):
        """
        Validate integer is between low and high values
        :param low: (int) Low range
        :param high: (int) High range
        :param type: (class) Data type, ex int, float
        :return: argument, exception
        """

        def number_range_parser(argument):
            try:
                argument = obj_type(argument)
            except ValueError:
                argparse.ArgumentError('Must be of type {}'.format(obj_type.__name__))

            if low <= argument <= high:
                return argument
            else:
                parser.error('Value is not in the range of {} and {}'.format(low, high))

        return number_range_parser


    # Create parser
    parser = argparse.ArgumentParser(description='Description of the program',
                                     formatter_class=parser_formatter(
                                         argparse.RawTextHelpFormatter,
                                         indent_increment=4, max_help_position=12, width=160))

    """
    Paths
    """
    # Directory
    parser.add_argument('-p', '--path', type=directory,
                        action='store', dest='path', default=Path('~/Downloads').expanduser(),
                        metavar='PATH_TO_DIR',
                        help='Path to folder/directory\n'
                             'Default: $HOME/Downloads')

    # File Read
    parser.add_argument('-r', '--file-read', type=argparse.FileType('r'),
                        action='store', dest='file_in', default=None,
                        metavar='PATH_TO_FILE',
                        help='File to read')
    # File write
    parser.add_argument('-w', '--file-write', type=argparse.FileType('w'),
                        action='store', dest='file_out', default=None,
                        metavar='PATH_TO_FILE',
                        help='File to write')

    """
    Numbers
    """
    # Single Integer
    parser.add_argument('-i1', '--integer', type=int,
                        action='store', dest='integer', default=10,
                        metavar='INTEGER',
                        help='Whole number\n'
                             'Default: Default: %(default)s')
    # Range Integer
    parser.add_argument('-i2', '--integer-in-range', type=number_range(0, 10),
                        action='store', dest='integer_range', default=10,
                        metavar='INTEGER',
                        help='Whole number form 0 to 10\n'
                             'Default: Default: %(default)s')
    # Single float
    parser.add_argument('-f1', '--float', type=float,
                        action='store', dest='float', default=10,
                        metavar='DECIMAL',
                        help='Decimal number\n'
                             'Default: Default: %(default)s')
    # Range Integer
    parser.add_argument('-f2', '--float-in-range', type=number_range(0.0, 1.0, float),
                        action='store', dest='float_range', default=1,
                        metavar='DECIMAL',
                        help='Decimal number form 0.0 to 1.0\n'
                             'Default: Default: %(default)s')

    """
    Strings
    """
    parser.add_argument('-s', '--string',
                        action='store', dest='string', default='test',
                        metavar='STRING',
                        help='String\n'
                             'Default: Default: %(default)s')

    """
    Multiple arguments
    """
    # Specific number
    parser.add_argument('-n1', '--nargs-2', type=int,
                        action='store', dest='nargs_two', default=[0, 10], nargs=2,
                        metavar='INTEGER',
                        help='2 integers\n'
                             'Default: %(default)s')
    # One or more (nargs='+')
    parser.add_argument('-n2', '--nargs-one-plus', type=float,
                        action='store', dest='nargs_one_plus', default=[0.0], nargs=argparse.ONE_OR_MORE,
                        metavar='INTEGER',
                        help='1 or more floats\n'
                             'Default: %(default)s')
    # Any number (nargs='*')
    parser.add_argument('-n3', '--nargs-zero-plus',
                        action='store', dest='nargs_zero_plus', default=[], nargs=argparse.ZERO_OR_MORE,
                        metavar='INTEGER',
                        help='Any amount of strings\n'
                             'Default: %(default)s')

    """
    Required
    """
    parser.add_argument('-e', '--req', type=int,
                        action='store', dest='required',
                        metavar='INTEGER',
                        help='Required option'
                             '\nDefault: %(default)s',
                        required=True)

    """
    Mutual exclusive
    """
    # Only one of the options in the set
    agree = parser.add_mutually_exclusive_group()
    agree.add_argument('--yes',
                       action='store_true', dest='bool', default=None,
                       help='Yes')

    agree.add_argument('--no',
                       action='store_false', dest='bool', default=None,
                       help='No')

    """
    Hidden
    """
    parser.add_argument('--debug',
                        action='store_true', dest='debug', default=False,
                        help=argparse.SUPPRESS)

    """
    Positional arguments
    """
    parser.add_argument('positional', metavar='N', nargs=argparse.ZERO_OR_MORE,
                        help='Positional arguments')

    options = parser.parse_args()

    main()
