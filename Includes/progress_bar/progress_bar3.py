#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script:	progress_bar3.py
Date:	2018-09-24

Platform: MacOS

Description:
Creates a text based progress bar
Customisable colour, title and header
Shows percentage.

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2018, thedzy'
__license__ = 'GPL'
__version__ = '3.1.5'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'

import os
import time


def progressbar(position, max_size=100, title='Loading', rgb=[1.0, 0.0, 0.0]):
    """
    Draw a progress bar to the width of the screen

    :param position: (int) Position relative to max value
    :param max_size: (int) Max position
    :param title: (str) Title at the beginning of the progress
    :param rgb: (tuple)float) The colour of the bar in decimal format of [0,0,0] - [1,1,1]
    :return: (void)
    """

    colour = get_colour(*rgb)

    try:
        columns, _ = os.get_terminal_size()
    except OSError:
        columns = 100

    progress_width = columns - 10 - len(title)
    progress_filled = int(position * progress_width / max_size)
    progress_empty = progress_width - progress_filled

    print('{title:s} [\033[38;5;{colour:0.0f}m{fill:s}{empty:s}\033[38;5;15m] {percent:4.1f}%'.format(
        colour=colour,
        fill='▉' * progress_filled,
        empty=' ' * progress_empty,
        percent=(position / max_size * 100),
        title=title
    ), end='\r', flush=True)


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
