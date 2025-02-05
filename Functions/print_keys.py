import logging
from datetime import datetime, timedelta
import random



def print_keys(dict_obj, indent:int=1, printer: callable = print):
    """
    Pretty print a dictionary (simplistic) (recursive)
    :param dict_obj: (dict) Object to parse
    :param indent: (int) Indent level
    :param filters: (list) Hide value if value does not match pattern
    :return: (int) Count of filters matched
    """

    def clean_key(key):
        if isinstance(key, str):
            return key.replace('_', ' ').title()
        else:
            return str(key)

    str_indent = '\t' * indent
    for key, value in dict_obj.items():
        if isinstance(dict_obj[key], dict):
            printer(f'{str_indent}{clean_key(key)}')
            print_keys(dict_obj[key], indent + 1)
        elif isinstance(dict_obj[key], list):
            printer(f'{str_indent}{clean_key(key)}')
            for item in dict_obj[key]:
                if isinstance(item, dict):
                    print_keys(item, indent + 1)
                else:
                    printer(f'\t{str_indent}{item}')
        else:
            if 'api.github' not in str(value):
                printer(f'{str_indent}{clean_key(key)}: {value}')


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


print_keys(test_json)