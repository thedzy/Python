#!/usr/bin/env python3

__author__ = 'Shane Young'
__version__ = '1.0'
__email__ = 'thedzy@hotmail.com'
__date__ = '2024-01-11'
__credits__ = ''

__description__ = \
    """
    flatten_dict.py: 
    Flatten dictionaries into single level key pairs
    Particularly useful for dictionaries to csvs
    """

from datetime import datetime, timedelta
import pprint


def flatten_dict(obj, seperator='->', formatters={}, format_strings=('{k}', '{k}{seperator}{sub_key}')) -> None:
    def handle(k, v):
        copy_obj = {}
        new_obj = flatten_dict(v, seperator)
        for sub_key, sub_value in new_obj.items():
            if type(sub_value) in formatters.keys():
                sub_value = formatters[type(sub_value)](sub_value)
            if sub_key is None:
                copy_obj[f'{k}'] = sub_value
            else:
                copy_obj[f'{k}{seperator}{sub_key}'] = sub_value
        return copy_obj

    if isinstance(obj, (list, tuple, set, frozenset)):
        copy_obj = {}
        for key, value in enumerate(obj):
            copy_obj.update(handle(key, value))
        return copy_obj
    elif isinstance(obj, dict):
        copy_obj = {}
        for key, value in obj.items():
            copy_obj.update(handle(key, value))
        return copy_obj
    else:
        return {None: obj}



test_json = {
    'key': 'value',
    'dict_key': {
        'sub_dict_key_1': 1,
        'sub_sub_dict_key': {
            '1': 2,
            '3': 4,
            'sub_sub_sub_dict_key': {
                '1': 2,
                '3': 4,
                'list': [1, 2, 3, {4: 4}]
            },
            0: '0'
        },
        'null_value': None,
        'bool_value': True,
        'tuple': ('Shane', 'jane'),
        'complex_number': 4j + 6j,
        'set': set([3, 4, 5, 6, 7]),
        'frozenset': frozenset([3, 4, 5, 6, 7]),
        'generator': [x for x in range(0, 11) if x % 2 == 0],
        'sub_key_int_1': 1,
        'sub_key_str_2': '2',
        'sub_key_float_3': 3.00,
        'Sub_list': [
            1, 2, {3: 3, 4: 4, 5: 5, 'more': [6, 7, 8, 9]}, 4, 5, 6
        ],
        'empty_list': [],
        'empty_dict': {},
        'date_time': {
            'start': datetime.now(),
            'end': datetime.now() - timedelta(days=30)
        }
    },
    'martrix': [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]

    ]
}

pprint.pp(test_json)
pprint.pp(flatten_dict(test_json, seperator=' '))

# use a method to format a class type in this case str(int) and str(datetime)
pprint.pp(flatten_dict(test_json, seperator='_', formatters={int: str, datetime: str}))


# use a method to format a class type in this case convert_date(datetime)
def convert_date(date):
    return date.strftime('%Y-%m-%dT%H:%M:%S')


pprint.pp(flatten_dict(test_json, seperator='/', formatters={datetime: convert_date}))

