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
__author__      = "thedzy"
__copyright__   = "Copyright 2018, thedzy"
__license__     = "GPL"
__version__     = "3.0"
__maintainer__  = "thedzy"
__email__       = "thedzy@hotmail.com"
__status__      = "Developer"

import time
import os, sys

def progressbar(position, max=100, title="Loading", rgb=[1.0,1.0,1.0]):
    """
    Draw a progress bar to the width of the screen

    :param position: Position relative to mac value
    :param max: Max position
    :param title: Title at the end of the progress
    :param rgb: The colour of the bar in decimal format of [0,0,0] - [1,1,1]
    :return: void
    """

    colour = (16 + (36 * rgb[0]) + (6 * rgb[1]) + rgb[2])

    rows, columns = os.popen('stty size', 'r').read().split()
    prog_width = int(columns) - 10 - len(title)
    prog_unit = (prog_width / max)
    prog_filled = int(prog_unit * position)
    prog_empty = prog_width - prog_filled

    print(" [\033[38;5;%dm%s%s\033[38;5;15m] %3d%%%s" % (colour, "▉" * prog_filled, " " * prog_empty, position/max*100, title), end="\r", flush = True)
