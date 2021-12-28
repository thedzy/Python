#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script:	progress_bar4.py
Date:	2018-09-24

Platform: MacOS

Description:
Customisable start colour and end colour
Title and header
Symbols/symbols
Shows percentage.

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2018, thedzy'
__license__ = 'GPL'
__version__ = '4.1'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'

import os


def progressbar(position, max_size=100, title='Loading', start=(0.0, 0.0, 0.0), end=(1.0, 1.0, 1.0), columns=None,
                ramp=None, color32=True, stepped=False):
    """
    Draw a progress bar to the width of the screen
    :param position: (int) Position relative to max value
    :param max_size: (int) Max position
    :param title: (str) Title at the start of the progress
    :param start: (tuple) The start colour of the bar in decimal format of [0,0,0] - [1,1,1]
    :param end: (tuple) The end colour of the bar in decimal format of [0,0,0] - [1,1,1]
    :param columns: (int) Progress display size, None for full width
    :param ramp: (str) Characters to use for the bar
    :param color32: (bool) Use 32 bit colour of 216 colours
    :param stepped: (bool) Use a colour for each character is the ramp vs a colour of each character in the bar
    :return: (void)
    """
    if ramp is None or len(ramp) == 0:
        ramp = '▁▂▃▄▅▆▇█'

    ramps = len(ramp)

    if not columns:
        try:
            columns, _ = os.get_terminal_size()
            columns = columns - (10 + len(title))
        except OSError:
            columns = 100

    ramp_steps = columns / ramps

    ramp_text = ''
    for index in range(0, ramps):
        tmp_ramp_section = f'{ramp[index] * (int(ramp_steps * (index + 1)) - int(ramp_steps * index) + 1)}'
        ramp_section = ''

        if stepped:
            red = start[0] + (((end[0] - start[0]) / ramps) * (index + 1))
            green = start[1] + (((end[1] - start[1]) / ramps) * (index + 1))
            blue = start[2] + (((end[2] - start[2]) / ramps) * (index + 1))

            for character in tmp_ramp_section:
                if color32:
                    ramp_section += f'\033[38;2;{red * 255:03.0f};{green * 255:03.0f};{blue * 255:03.0f}m{character}'
                else:
                    colour = get_colour(red, green, blue)
                    ramp_section += f'\033[38;5;{colour:03}m{character}'
        else:
            ramp_section = tmp_ramp_section

        ramp_text = f'{ramp_text}{ramp_section}'

    if not stepped:
        new_ramp_text = ''
        for index, character in enumerate(ramp_text):
            red = start[0] + (((end[0] - start[0]) / columns) * (index + 1))
            green = start[1] + (((end[1] - start[1]) / columns) * (index + 1))
            blue = start[2] + (((end[2] - start[2]) / columns) * (index + 1))
            if color32:
                new_ramp_text += f'\033[38;2;{red * 255:03.0f};{green * 255:03.0f};{blue * 255:03.0f}m{character}'
            else:
                colour = get_colour(red, green, blue)
                new_ramp_text += f'\033[38;5;{colour:03}m{character}'

        ramp_text = new_ramp_text

    if color32:
        block_length = 20
    else:
        block_length = 12

    fill_spaces = int((columns / max_size) * position)
    fill = ramp_text[:(fill_spaces * block_length)]
    empty = ' ' * (columns - fill_spaces)
    percent = int(position / max_size * 100)

    print(f'{title} [{fill}{empty}\033[0m] {percent:3}%', end='\r', flush=True)

    return


def get_colour(red, green, blue):
    """
    Calculate ansi code for rgb
    :param red: (float) 0-1 Red
    :param green: (float) 0-1 Green
    :param blue: (float) 0-1 Blue
    :return: (int) 0-255 Ansi code
    """
    if int(red * 5) == int(green * 5) == int(blue * 5):
        # If colour is shade of grey
        ansi_code = 232 + (int(red * 23) + int(green * 23) + int(blue * 23)) // 3
    else:
        # If colour
        ansi_code = (16 + int(36 * red * 5) + int(6 * green * 5) + int(blue * 5))

    return ansi_code
