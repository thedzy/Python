#!/usr/bin/env python3

import sys

# Check that stdin is not empty, and loop through lines in stdin
if not sys.stdin.isatty():
    for stdin_line in sys.stdin.read().split('\n'):
        print(stdin_line)