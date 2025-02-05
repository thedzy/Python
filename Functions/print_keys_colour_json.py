import json
from datetime import datetime, timedelta


def print_json(dict_obj, key_colour='blue', key_bold=True, key_inverted=False,
               value_colour='green', value_bold=True, value_inverted=False,
               other_colour='white', other_bold=False, other_inverted=False,
               indents=2, line_breaks=True, _indent=0):
    """
    Pretty print a dictionary (simplistic) (recursive)
    :param dict_obj: (dict) Object to parse
    :param _indent: (int) Indent level
    :param filters: (list) Hide value if value does not match pattern
    :return: (int) Count of filters matched
    """
    end = '\n' if line_breaks else ' '

    kwargs = {
        'key_colour': key_colour,
        'key_bold': key_bold,
        'key_inverted': key_inverted,
        'value_colour': value_colour,
        'value_bold': value_bold,
        'value_inverted': value_inverted,
        'other_colour': other_colour,
        'other_bold': other_bold,
        'other_inverted': other_inverted,
        'line_breaks': line_breaks,
        'indents': indents
    }

    def get_colour(colour='none', bold=False, inverted=False):
        """
        Get the colour is specified by name
        :param colour:
        :param bold:
        :param inverted:
        :return:
        """
        colours = dict(
            black='\x1B[30m',
            red='\x1B[31m',
            green='\x1B[32m',
            yellow='\x1B[33m',
            blue='\x1B[34m',
            magenta='\x1B[35m',
            cyan='\x1B[36m',
            white='\x1B[37m',
            none='\x1B[0m'
        )
        if colour in colours:
            temp_colour = colours['none']
            temp_colour += colours[colour]
            if bold:
                temp_colour += "\x1B[1m"
            if inverted:
                temp_colour += "\x1B[7m"
            # temp_colour += colours['none']
        else:
            return colour

        return temp_colour

    key_colour = get_colour(key_colour, key_bold, key_inverted)
    value_colour = get_colour(value_colour, value_bold, value_inverted)
    other_colour = get_colour(other_colour, other_bold, other_inverted)

    def str_indent(i):
        return ' ' * (_indent * indents)

    if _indent == 0:
        print(f'{str_indent(_indent)}{other_colour}{{', end=end)
        _indent += 1

    for index, key_value in enumerate(dict_obj.items()):
        key, value = key_value
        if isinstance(dict_obj[key], dict):
            print(f'{str_indent(_indent)}{key_colour}"{key}"{other_colour}: {{', end=end)
            print_json(dict_obj[key], _indent=_indent + 1, **kwargs)
            print(f'{str_indent(_indent)}}},', end=end)
        elif isinstance(dict_obj[key], (list, tuple, set )):
            if isinstance(dict_obj[key], list):
                brackets = '[]'
            elif isinstance(dict_obj[key], tuple):
                brackets = '()'
            elif isinstance(dict_obj[key], set):
                brackets = '{}'
            print(f'{str_indent(_indent)}{key_colour}"{key}"{other_colour}: {brackets[0]}', end=end)
            for index, item in enumerate(dict_obj[key]):
                if isinstance(item, str):
                    item = f'{value_colour}"{item}"{other_colour}'
                if isinstance(item, dict):
                    print_json(item, _indent=_indent + 1, **kwargs)
                else:
                    print(f'{" " * indents}{str_indent(_indent)}{item}{"" if index + 1 == len(dict_obj[key]) else ","}', end=end)
            print(f'{str_indent(_indent)}{brackets[1]}{"" if index + 1 == len(dict_obj[key]) else ","} ', end=end)
        else:
            if isinstance(value, str):
                value = f'{value_colour}"{value}"{other_colour}'
            print(f'{str_indent(_indent)}{key_colour}"{key}"{other_colour}: {value}{"" if index + 1 == len(dict_obj.items()) else ","}', end=end)

    if _indent <= 1:
        _indent -= 1
        print(f'{str_indent(_indent)}{other_colour}}}{get_colour()}', end=end)


test_json = {
    "key": "value",
    "dict_key": {
        "sub_key_1": 1,
        "sub_key_2": "2",
        "sub_key_3": "value",
        "Sub_list": [
            1, 2, 3, 4, 5, 6
        ],
        "times": {
            "start": datetime.now(),
            "end": datetime.now() - timedelta(days=30)
        }
    }
}

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

print_json(test_json, key_colour='yellow', indents=2)
