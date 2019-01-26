#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script:	progress_bar4.py
Date:	2018-09-24

Platform: MacOS

Description:
Customisable colour, title and header
Shows percentage.

"""
__author__      = "thedzy"
__copyright__   = "Copyright 2018, thedzy"
__license__     = "GPL"
__version__     = "4.0"
__maintainer__  = "thedzy"
__email__       = "thedzy@hotmail.com"
__status__      = "Developer"

import time
import os, sys

def progressbar(position, max=100, title="Loading", rgba=[0.0,0.0,0.0], rgbb=[0.0,1.0,0.0]):
    """
    Draw a progress bar to the width of the screen

    :param position: Position relative to mac value
    :param max: Max position
    :param title: Title at the end of the progress
    :param rgba: The startcolour of the bar in decimal format of [0,0,0] - [1,1,1]
    :param rgbb: The startcolour of the bar in decimal format of [0,0,0] - [1,1,1]
    :return: void
    """

    # Calculate values
    rows, columns = os.popen('stty size', 'r').read().split()
    prog_width = int(columns) - 10 - len(title)
    prog_unit = (prog_width / max)
    prog_filled = int(prog_unit * position)
    prog_empty = prog_width - prog_filled

    # Calculate colours
    red   = abs((rgbb[0] -rgba[0]) * (position / (max + 1)) + rgba[0])
    green = abs((rgbb[1] -rgba[1]) * (position / (max + 1)) + rgba[1])
    blue  = abs((rgbb[2] -rgba[2]) * (position / (max + 1)) + rgba[2])
    colour = int(16 + (36 * red) + (6 * green) + blue)
    #print(str(red) + ", " + str(green) + ", " + str(blue))
    #print(str(colour))

    # Draw progress
    print(" [\033[38;5;%dm%s%s\033[38;5;15m] %3d%% %s" % (colour, "▉" * prog_filled, " " * prog_empty, position/max*100, title), end="\r", flush = True)
