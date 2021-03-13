#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script:	progress_bar2.py
Date:	2018-09-24

Platform: MacOS

Description:
Creates a dead simple inline text based progress bar
Customisable title

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2018, thedzy'
__license__ = 'GPL'
__version__ = '2.1'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'

import os
import sys
import time

title = 'Loading'
progress_max = 33

try:
    columns, _ = os.get_terminal_size()
except OSError:
    columns = 100
progress_width = int(columns) - 3 - len(title)
progress_width = (progress_max * int(progress_width / progress_max))

# Setup toolbar
sys.stdout.write('[{}] {}'.format(' ' * progress_width, title))
sys.stdout.flush()
# Return to start of line, after '['
sys.stdout.write('\b' * (progress_width + len(title) + 2))

for i in range(progress_max):
    # Do real work here
    time.sleep(0.05)
    # Update the bar
    sys.stdout.write('{}'.format('▉' * (progress_width // progress_max)))
    sys.stdout.flush()

sys.stdout.write('\n')
