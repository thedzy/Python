import random
from datetime import datetime, timedelta
import logging
import random

def print_tree(dict_obj, indent='', style=0, null=None, width=0,
               printer=print):
    """
    Pretty print a dictionary (simplistic) (recursive)
    :param dict_obj: (dict) Object to parse
    :param indent: (int) Indent level
    :param filters: (list) Hide value if value does not match pattern
    :return: (int) Count of filters matched
    """

    # Set looks
    inset = ' ' * width if len(indent) > 0 else ''
    styles = [
        dict(
            mid=inset + '├─', end=inset + '└─', cont=inset + '│ ', none=inset + '  ', unnamed='─' * width + '┐ ', null=inset + '┘'
        ),
        dict(
            mid=inset + '┠─', end=inset + '┖─', cont=inset + '┃ ', none=inset + '  ', unnamed='─' * width + '┒ ', null=inset + '┘'
        ),
        dict(
            mid=inset + '┣━', end=inset + '┗━', cont=inset + '┃ ', none=inset + '  ', unnamed='━' * width + '┓ ', null=inset + '┛'
        ),
        dict(
            mid=inset + '╟─', end=inset + '╙─', cont=inset + '║ ', none=inset + '  ', unnamed='─' * width + '╖ ', null=inset + '┘'
        ),
        dict(
            mid=inset + '╠═', end=inset + '╚═', cont=inset + '║ ', none=inset + '  ', unnamed='═' * width + '╗ ', null=inset + '╝'
        ),
        dict(
            mid=inset + '├─', end=inset + '╰─', cont=inset + '│ ', none=inset + '  ', unnamed='─' * width + '╮ ', null=inset + '╯'
        ),
        dict(
            mid=inset + '╏╺', end=inset + '┗╺', cont=inset + '╏ ', none=inset + '  ', unnamed='╺' * width + '┓ ', null=inset + '╸╸╸╸'
        )
    ]
    if style >= len(styles):
        style = 0
    if not null:
        null = styles[style]['null']

    # Get indent symbols
    def symb(i, l):
        return styles[style]['mid'] if i + 1 != l else styles[style]['end']

    def next_symb(i, l):
        return styles[style]['cont'] if i + 1 != l else styles[style]['none']

    # Format keys
    def format_key(k):
        return f'{k}'

    def format_value(v):
        if isinstance(v, str):
            return f'"{v}"'
        else:
            return f'{v}'

    # Draw keys and values
    length = len(dict_obj)
    if isinstance(dict_obj, dict):
        if length == 0:
            printer(f'{indent}{symb(0, 1)}{null}')
        for index, key_value in enumerate(dict_obj.items()):
            key, value = key_value
            if isinstance(dict_obj[key], dict):
                printer(f'{indent}{symb(index, length)} {format_key(key)}')
                print_tree(dict_obj[key], indent + next_symb(index, length), style=style, null=null,
                           printer=printer)
            elif isinstance(dict_obj[key], list):
                printer(f'{indent}{symb(index, length)} {format_key(key)}')
                print_tree(dict_obj[key], indent + next_symb(index, length), style=style, null=null,
                           printer=printer)
            else:
                printer(f'{indent}{symb(index, length)} {format_key(key)} = {format_value(value)}')
    if isinstance(dict_obj, list):
        if length == 0:
            printer(f'{indent}{symb(0, 1)}{null}')
        for index, value in enumerate(dict_obj):
            if isinstance(value, dict):
                printer(f'{indent}{symb(index, length)}{styles[style]["unnamed"]} ')
                print_tree(value, indent + next_symb(index, length), style=style, null=null,
                           printer=printer)
            elif isinstance(value, list):
                printer(f'{indent}{symb(index, length)}{styles[style]["unnamed"]} ')
                print_tree(value, indent + next_symb(index, length), style=style, null=null,
                           printer=printer)
            else:
                printer(f'{indent}{symb(index, length)} {format_value(value)}')


test_json = {
    'key': 'value',
    'dict_key': {
        'sub_key_1': 1,
        'sub_sub_key': {
            '1': 2,
            '3': 4,
            'sub_sub_sub_key': {
                '1': 2,
                '3': 4,
                'list': [1, 2, 3, { 4:4 }]
            },
            0: '0'
        },
        'null_value': None,
        'bool_value': True,
        'sub_key_2': '2',
        'sub_key_3': 'value',
        'Sub_list': [
            1, 2, {3:3}, 4, 5, 6
        ],
        'empty_list': [],
        'empty_dict': {},
        'times': {
            'start': datetime.now(),
            'end': datetime.now() - timedelta(days=30)
        }
    }
}


logging.basicConfig(filename=None, format='[{asctime}] [{levelname:7}] {message}', style='{', level=10)


print_tree(test_json, style=random.randint(0,11), printer=logging.info)
