#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script:	progress_bar3b.py
Date:	2021-12-17

Platform: MacOS

Description:
Creates a text based progress bar
Customisable colour, and text
Dynamically chooses text colour for bar colour
Shows percentage.
Similar to v6 without Gui


"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2018, thedzy'
__license__ = 'GPL'
__version__ = '3.2'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'

import os


def progress_bar(position, max_size=100, title='Loading...', rgb=(1.0, 1.0, 1.0), columns=None):
    """
    Draw a progress bar to the width of the screen
    :param position: (int) Position relative to max value
    :param max_size: (int) Max position
    :param title: (str) Title at the beginning of the progress
    :param rgb: (tuple)float) The colour of the bar in decimal format of [0,0,0] - [1,1,1]
    :param columns: (int) Width of the progressbar or None for the size of the window
    :return: (void)
    """

    # Get the 216 colour code for the rgb
    colour = get_colour(*rgb)
    contrast = colour_contrast(*rgb)

    if contrast > 0.5:
        text_colour = 233
    else:
        text_colour = 255

    if not columns:
        try:
            columns, _ = os.get_terminal_size()
        except OSError:
            columns = 100

    # Define paddings
    title_padding, bar_padding = 7, 2

    # Get width and fill size
    progress_width = columns - bar_padding
    progress_filled = int(position * progress_width / max_size)

    # Trim title if too long and format
    if len(title) > progress_width - title_padding:
        title = f'...{title[-progress_width + title_padding + 3:]}'
    progress_text = f'[{title.ljust(progress_width - title_padding)} {progress_filled / progress_width * 100:3.0f}%]'
    fill = progress_text[0:progress_filled]
    empty = progress_text[progress_filled:columns]

    # Print
    print(f'\033[48;5;{text_colour}m\033[38;7m\033[38;5;{colour:0.0f}m{fill}\033[38;0m{empty}\033[0m', end='\r',
          flush=True)


def wait_bar(offset, title='Loading...', rgb=(1.0, 1.0, 1.0), columns=None, pattern=' ◢◤ ', left2right=True):
    """
    Draw a progress bar to the width of the screen
    :param offset: (int) Position offset
    :param title: (str) Title at the beginning of the progress
    :param rgb: (tuple)float) The colour of the bar in decimal format of [0,0,0] - [1,1,1]
    :param columns: (int) Width of the progressbar or None for the size of the window
    :param pattern: (str) The characters for the wait
    :param left2right: (bool) Movement for left r=to right
    :return: (void)
    """

    # Get the 216 colour code for the rgb
    fore_colour = get_colour(*rgb)

    if not columns:
        try:
            columns, _ = os.get_terminal_size()
            columns = columns - (5 + len(title))
        except OSError:
            columns = 100

    # Calculate for direction
    pattern_len = len(pattern)
    if left2right:
        start = pattern_len - (offset % pattern_len)
    else:
        start = offset % pattern_len

    # Repeat pattern
    text = f'{pattern[start:]}{pattern[:start]}' * columns

    # Print
    print(f'\033[0m {title} \033[0m\033[38;5;{fore_colour}m[{text[:columns]}]\033[0m', end='\r', flush=True)


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


def colour_contrast(red, green, blue):
    """
    Get the perceived brightness of a colour
    :param red: (float) 0-1 Red
    :param green: (float) 0-1 Green
    :param blue: (float) 0-1 Blue
    :return: (int) 0-1 Perceived brightness
    """

    colour_value = ((red * 299) + (green * 587) + (blue * 114)) / 1000

    return colour_value
