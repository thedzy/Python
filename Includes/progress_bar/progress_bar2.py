#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script:	progress_bar2.py
Date:	2018-09-24

Platform: MacOS

Description:
Creates a text based progress bar
Customisable title

"""
__author__      = "thedzy"
__copyright__   = "Copyright 2018, thedzy"
__license__     = "GPL"
__version__     = "2.0"
__maintainer__  = "thedzy"
__email__       = "thedzy@hotmail.com"
__status__      = "Developer"

import os
import sys
import time

title = "Loading"
prog_max = 33

rows, columns = os.popen('stty size', 'r').read().split()
prog_width = int(columns) - 3 - len(title)
prog_width = (prog_max * int(prog_width/prog_max))

# setup toolbar
sys.stdout.write("[%s] %s" % (" " * prog_width, title))
sys.stdout.flush()
# return to start of line, after '['
sys.stdout.write("\b" * (prog_width + len(title) + 2))

for i in xrange(prog_max):
    # do real work here
    time.sleep(0.05)
    # update the bar
    sys.stdout.write("%s" % ("▉" * int(prog_width/prog_max)))
    sys.stdout.flush()

sys.stdout.write("\n")
