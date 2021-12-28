#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from progress_bar3b import *
import glob


def main():
    # Speed of wait
    seconds = 5

    # Run a few waits
    loops = 200
    for index in range(loops):
        # Do real work here
        wait_bar(index,
                 title=f'Time left: {seconds - (index * (seconds / loops)):0.0f}',
                 rgb=(1, 0, 1),
                 columns=14,
                 pattern='▁▂▂▃▄▅▆▇▇█▇▇▆▅▄▃▂▂')
        time.sleep(seconds / loops)
    print(' ' * 50, end='\r')

    loops = 30
    for index in range(loops):
        # Do real work here
        wait_bar(index,
                 title=f'Time left: {seconds - (index * (seconds / loops)):0.0f}',
                 rgb=(0.5, 0.5, 0),
                 columns=20,
                 pattern='  ▜▙ ')
        time.sleep(seconds / loops)
    print(' ' * 50, end='\r')

    loops = 30
    for index in range(loops):
        # Do real work here
        wait_bar(index,
                 rgb=(1, 1, 1),
                 columns=15,
                 pattern='🚙🚗🚛🏎🛻🚑🚕🚚🚒',
                 left2right=False)
        time.sleep(seconds / loops)
    print(' ' * 50, end='\r')

    loops = 100
    for index in range(loops):
        # Do real work here
        wait_bar(index,
                 rgb=(1, 1, 1),
                 columns=15,
                 pattern='>>-----')
        time.sleep(seconds / loops)
    print()

    # Speed of progress
    seconds = 2

    files = glob.glob('/Applications/*')
    progress_length = len(files)

    # Darker colour run
    for index, file in enumerate(files):
        # Do real work here
        progress_bar(index + 1, progress_length, file, [0.1, 0.1, 0.25])
        time.sleep(seconds / progress_length)
    print()

    # Lighter colour run
    progress_length = 100
    for index in range(progress_length):
        # Do real work here
        progress_bar(index + 1, columns=50)
        time.sleep(seconds / progress_length)
    print()


if __name__ == '__main__':
    main()
