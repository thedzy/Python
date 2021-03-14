#!/usr/bin/env python3


from popup_spin import *


def main():
    quantity, exit_code = PopupSpin('Quantity', 'How many do you need?', 10, 20).get_input()

    if exit_code:
        print('Quantity: %s\nExit Code: %d\n' % (quantity, exit_code))
    else:
        print('Exited')


if __name__ == '__main__':
    main()
