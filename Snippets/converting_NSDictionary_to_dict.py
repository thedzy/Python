#!/usr/bin/env python3

import json
from SystemConfiguration import *
from Foundation import __NSCFDictionary
from Foundation import __NSCFArray
from PyObjCTools import Conversion


def convert_to_dict(old_dict, new_dict):
    if isinstance(old_dict, __NSCFDictionary):
        try:
            for key in old_dict:
                if isinstance(old_dict[key], __NSCFArray):
                    new_dict[key] = []
                    convert_to_dict(old_dict[key], new_dict[key])
                elif isinstance(old_dict[key], __NSCFDictionary):
                    new_dict[key] = {}
                    convert_to_dict(old_dict[key], new_dict[key])
                else:
                    new_dict[key] = old_dict[key]
        except:
            return

    if isinstance(new_dict, list):
        for key in old_dict:
            if isinstance(key, __NSCFArray):
                new_array = []
                new_dict.append(new_array)
                convert_to_dict(old_dict[key], new_array)
            elif isinstance(key, __NSCFDictionary):
                new_dict[key] = {}
                convert_to_dict(old_dict[key], new_dict[key])
            else:
                new_dict.append(key)


def change_termainal_font(**kwargs):
    fgcolour = kwargs.get('fgcolour', "white")
    bgcolour = kwargs.get('bgcolour', "black")
    style = kwargs.get('style', "normal")
    reset = kwargs.get('reset', False)

    font_style = {
        'normal': 0,
        'bold': 1,
        'Underline': 2,
        'Negative1': 3,
        'Negative2': 5,
    }

    fg_colours = {
        'black': 30,
        'red': 31,
        'green': 32,
        'yellow': 33,
        'blue': 34,
        'purple': 35,
        'cyan': 36,
        'light gray': 37,
        'dark gray': 90,
        'light red': 91,
        'light green': 92,
        'light yellow': 93,
        'light blue': 94,
        'light magenta': 95,
        'light cyan': 96,
        'white': 97,
    }

    bg_colours = {
        'black': 40,
        'red': 41,
        'green': 42,
        'yellow': 43,
        'blue': 44,
        'purple': 45,
        'cyan': 46,
        'light gray': 47,
        'dark gray': 100,
        'light red': 101,
        'light green': 102,
        'light yellow': 102,
        'light blue': 104,
        'light magenta': 105,
        'light cyan': 106,
        'white': 107,

    }

    if reset:
        print('\033[0m')
    else:
        print('\033[{0};{1};{2}m'.format(font_style.get(style, 0), fg_colours.get(fgcolour, 37), bg_colours.get(bgcolour, 40)))

# Get a NSDictionary
prefs = SCPreferencesCreate(None, "", None)
network = SCPreferencesPathGetValue(prefs,'/NetworkServices')

# Display the NSDictionary
change_termainal_font(fgcolour='white', style='bold', bgcolour='red')
print("=" * 40)
print('Before')
print("=" * 40)
print(network)

# Display the python dictionary
change_termainal_font(fgcolour='white', style='bold', bgcolour='green')
print("=" * 40)
print('After with function')
print("=" * 40)
new_dict = {}
convert_to_dict(network, new_dict)
print(json.dumps(new_dict, indent=4))

# Display the python dictionary using the conversion tool
change_termainal_font(fgcolour='white', style='bold', bgcolour='blue')
print("=" * 40)
print('After with PyObjCTools')
print("=" * 40)
print(json.dumps(Conversion.pythonCollectionFromPropertyList(network), indent=4))
print("=" * 40)

change_termainal_font(reset=True)