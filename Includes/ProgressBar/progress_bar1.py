#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os, sys

rows, columns = os.popen('stty size', 'r').read().split()
toolbar_width = int(columns) - 5

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("▉")
    sys.stdout.flush()

sys.stdout.write("\n")