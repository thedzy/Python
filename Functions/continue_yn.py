#!/usr/bin/env python3

import sys
import termios
import tty


def continue_yn(message: str = 'Continue (y/n)?', printer=print) -> bool:
    """
    Ask user to continue or not
    :param message: Message to display
    :return: True if user wants to continue, False otherwise
    """
    printer(message, end='\r')
    # Get file descriptor for stdin
    fd = sys.stdin.fileno()

    # Save current terminal settings
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        char = ''
        while char.lower() not in ['y', 'n']:
            char = sys.stdin.read(1)
    finally:
        # Restore old terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print()

    return char.lower() == 'y'


if continue_yn():
    print('yes')
else:
    print('No')
