import logging
from datetime import datetime, timedelta
import random


def print_tree(dict_obj: dict, indent: str = '', style: int = 0, null: str = None,
               quote: str = '\'', equals='=',
               key_colour: str = 'blue', key_bold: bool = True, key_inverted: bool = False,
               value_colour: str = 'green', value_bold: bool = True, value_inverted: bool = False,
               other_colour: str = 'white', other_bold: bool = False, other_inverted: bool = False,
               printer: callable = print, width: int = 1, display_type: bool = False
               ) -> None:
    """
    Pretty print a dictionary as a tree (recursive)
    :param dict_obj: (dict) Object to parse
    :param indent: (int) Indent level
    :param style: (list) Hide value if value does not match pattern
    :param null: String to display for null values
    :param quote: String to display for quotes
    :param key_colour: Name of colour od escape sequence
    :param key_bold: Use bold colours
    :param key_inverted: Use inverted colours
    :param value_colour: Name of colour od escape sequence
    :param value_bold: Use bold colours
    :param value_inverted: Use inverted colours
    :param other_colour: Name of colour od escape sequence
    :param other_bold: Use bold colours
    :param other_inverted: Use inverted colours
    :param printer: Function to use for printing (ex logger.info)
    :param width: The indent width
    :param display_type: Display the value type with the value
    :return: None
    """
    kwargs = {
        'style': style,
        'null': null,
        'key_colour': key_colour,
        'key_bold': key_bold,
        'key_inverted': key_inverted,
        'quote': quote,
        'equals': equals,
        'value_colour': value_colour,
        'value_bold': value_bold,
        'value_inverted': value_inverted,
        'other_colour': other_colour,
        'other_bold': other_bold,
        'other_inverted': other_inverted,
        'printer': printer,
        'width': width,
        'display_type': display_type
    }

    def get_style(s):
        symbols_sets = [
            ('├─', '└─', '│ ', '  ', '─' * width + '┐ ', '┘'),
            ('┠─', '┖─', '┃ ', '  ', '─' * width + '┒ ', '┘'),
            ('┣━', '┗━', '┃ ', '  ', '━' * width + '┓ ', '┛'),
            ('╟─', '╙─', '║ ', '  ', '─' * width + '╖ ', '┘'),
            ('╠═', '╚═', '║ ', '  ', '═' * width + '╗ ', '╝'),
            ('├─', '╰─', '│ ', '  ', '─' * width + '╮ ', '╯'),
            ('╏╺', '┗╺', '╏ ', '  ', '╺' * width + '┓ ', '╸╸╸╸'),
            ('▕╲', ' ╲', '▕ ', '  ', '▁' * width + '▁ ', '╳╳╳╳╲'),
            (' -', ' -', ' ', '  ', '-' * width + '  ', ' -- '),
        ]
        if s >= len(symbols_sets):
            s = 0

        inset = ' ' * width if len(indent) > 0 else ''

        return {
            'mid': inset + symbols_sets[s][0],
            'end': inset + symbols_sets[s][1],
            'cont': inset + symbols_sets[s][2],
            'none': inset + symbols_sets[s][3],
            'unnamed': symbols_sets[s][4],
            'null': symbols_sets[s][5]
        }

    null = get_style(style)['null'] if null is None else null

    # get colour
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

    # Get indent symbols
    def symbol(i, l):
        return f'{get_colour(other_colour, other_bold, other_inverted)}{get_style(style)["mid"] if i + 1 != l else get_style(style)["end"]}{get_colour()}'

    def next_symbol(i, l):
        return f'{get_colour(other_colour, other_bold, other_inverted)}{get_style(style)["cont"] if i + 1 != l else get_style(style)["none"]}{get_colour()}'

    # Format keys
    def format_key(k):
        if isinstance(k, str) and quote:
            return f'{get_colour(key_colour, key_bold, key_inverted)}{quote}{k}{quote}{get_colour()}'
        else:
            return f'{get_colour(key_colour, key_bold, key_inverted)}{k}{get_colour()}'

    def format_value(v):
        instance_type = f'({type(v).__name__})' if display_type else ''
        if isinstance(v, str):
            return f'{get_colour(value_colour, value_bold, value_inverted)}{quote}{v}{quote} {instance_type}{get_colour()}'
        else:
            return f'{get_colour(value_colour, value_bold, value_inverted)}{v} {instance_type}{get_colour()}'

    def format_type(t):
        instance_type = f'({type(t).__name__})' if display_type else ''
        return f'{get_colour(value_colour, value_bold, value_inverted)}{instance_type}{get_colour()}'

    def format_other(o):
        return f'{get_colour(other_colour, other_bold)}{o}{get_colour()}'

    # Draw keys and values
    length = len(dict_obj)
    if isinstance(dict_obj, dict):
        if length == 0:
            printer(f'{indent}{symbol(0, 1)}{format_other(null)}')
        for index, key_value in enumerate(dict_obj.items()):
            key, value = key_value
            if isinstance(dict_obj[key], dict):
                printer(f'{indent}{symbol(index, length)} {format_key(key)}')
                print_tree(dict_obj[key], indent + next_symbol(index, length), **kwargs)
            elif isinstance(dict_obj[key], (list, tuple, set, frozenset)):
                printer(f'{indent}{symbol(index, length)} {format_key(key)}')
                print_tree(dict_obj[key], indent + next_symbol(index, length), **kwargs)
            else:
                printer(f'{indent}{symbol(index, length)} {format_key(key)} {format_other(equals)} {format_value(value)}')
    if isinstance(dict_obj, (list, tuple, set, frozenset)):
        if length == 0:
            printer(f'{indent}{symbol(0, 1)}{format_other(null)}')
        for index, value in enumerate(dict_obj):
            if isinstance(value, dict):
                printer(f'{indent}{symbol(index, length)}{format_other(get_style(style)["unnamed"])} {format_type(dict_obj)}')
                print_tree(value, indent + next_symbol(index, length), **kwargs)
            elif isinstance(value, (list, tuple, set, frozenset)):
                printer(f'{indent}{symbol(index, length)}{format_other(get_style(style)["unnamed"])} {format_type(dict_obj)}')
                print_tree(value, indent + next_symbol(index, length), **kwargs)
            else:
                printer(f'{indent}{symbol(index, length)} {format_value(value)}')


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


colours = [
    'black',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white',
    'none',
]

# Print random samples
for sample in range(0, 3):
    style = random.randint(0, 8)
    quote = random.choice(("'", '"', ''))
    equals = random.choice(('=', '->', '>', '»', '›', ''))
    key_colour = random.choice(colours)
    key_bold = random.choice([True, False])
    value_colour = random.choice(colours)
    value_bold = random.choice([True, False])
    other_colour = random.choice(colours)
    other_bold = random.choice([True, False])
    printer = print
    width = random.randint(0, 8)
    display_type = random.choice((True, False))

    print(f'Random sample {sample}:')
    printer(f'print_tree(test_json, style={style},\n'
            f'\tquote="{quote}", equals="{equals}",\n'
            f'\tkey_colour="{key_colour}", key_bold={key_bold},\n'
            f'\tvalue_colour="{value_colour}", value_bold={value_bold},\n'
            f'\tother_colour="{other_colour}", other_bold={other_bold},\n'
            f'\tprinter={printer.__name__}, width={width}, display_type={display_type})')
    print_tree(test_json, style=style,
               quote=quote, equals=equals,
               key_colour=key_colour, key_bold=key_bold,
               value_colour=value_colour, value_bold=value_bold,
               other_colour=other_colour, other_bold=other_bold,
               printer=printer, width=width, display_type=display_type)
    printer('-' * 120)

# Predefined samples
random_sample = random.randint(0, 6)
print(f'Random predefined sample {random_sample}:')
if random_sample == 0:
    print_tree(test_json, style=5, quote='\'',
               key_colour='blue', key_bold=False,
               value_colour='yellow', value_bold=True,
               other_colour='white', other_bold=True,
               printer=print, width=2, display_type=False)

if random_sample == 1:
    print_tree(test_json, style=5, quote='', equals="=",
               key_colour='magenta', key_bold=False,
               value_colour='white', value_bold=True,
               other_colour='white', other_bold=True,
               printer=print, width=2, display_type=False)

if random_sample == 2:
    print_tree(test_json, style=0,
               quote="", equals='»',
               key_colour="black", key_bold=True,
               value_colour="blue", value_bold=True,
               other_colour="none", other_bold=True,
               printer=print, width=1, display_type=False)

if random_sample == 3:
    print_tree(test_json, style=1,
               quote="", equals="@",
               key_colour="white", key_bold=True,
               value_colour="black", value_bold=True,
               other_colour="white", other_bold=False,
               printer=print, width=3, display_type=False)

if random_sample == 4:
    print_tree(test_json, style=6,
               quote="", equals="=",
               key_colour="white", key_bold=False,
               value_colour="red", value_bold=False,
               other_colour="none", other_bold=True,
               printer=print, width=4, display_type=False)

if random_sample == 5:
    print_tree(test_json, style=5,
               quote="", equals="»",
               key_colour="green", key_bold=True,
               value_colour="white", value_bold=True,
               other_colour="magenta", other_bold=False,
               printer=print, width=5, display_type=False)

if random_sample == 6:
    print_tree(test_json, style=8,
               quote="", equals="»",
               key_colour="green", key_bold=True,
               value_colour="white", value_bold=True,
               other_colour="magenta", other_bold=False,
               printer=print, width=4, display_type=False)

varied_widths = False
if varied_widths:
    for width in range(0, 15):
        print_tree(test_json, style=5, quote='\'',
                   key_colour='blue', key_bold=False,
                   value_colour='yellow', value_bold=True,
                   other_colour='white', other_bold=True,
                   printer=print, width=width, display_type=False)

all_styles = False
if all_styles:
    for style in range(0, 9):
        print(style)
        print_tree(test_json, style=style, quote='\'',
                   key_colour='blue', key_bold=False,
                   value_colour='yellow', value_bold=True,
                   other_colour='white', other_bold=True,
                   printer=print, width=0, display_type=False)