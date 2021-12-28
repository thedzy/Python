#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from progress_bar4 import *
import time


def main():
    progress_length = 100
    speed = 1

    for item in range(progress_length):
        # do real work here
        time.sleep(speed / progress_length)
        progressbar(item + 1, ramp='▷▶', start=(0.0, 1.0, 0.0), end=(1.0, 1.0, 1.0), stepped=False)
    print()

    for item in range(progress_length):
        # do real work here
        time.sleep(speed / progress_length)
        progressbar(item + 1, columns=50, ramp='█', start=(0.0, 0.0, 0.0), end=(1.0, 1.0, 1.0), stepped=False, color32=False)
    print()

    for item in range(progress_length):
        # do real work here
        time.sleep(speed / progress_length)
        progressbar(item + 1, columns=50, start=(1.0, 0.0, 0.0), end=(0.0, 1.0, 0.0), color32=True, stepped=True)
    print()


if __name__ == '__main__':
    main()
