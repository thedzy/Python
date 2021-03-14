#!/usr/bin/env python3


from popup_input import *


def main():
    name, exit_code = PopupInput('Name', 'What is your name?').get_input()

    if exit_code:
        print('Name: %s\nExit Code: %d\n' % (name, exit_code))
    else:
        print('Exited')


if __name__ == '__main__':
    main()
