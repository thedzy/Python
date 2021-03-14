#!/usr/bin/env python3


from popup_scale import *


def main():
    quantity, exit_code = PopupScale('Quantity', 'How many do you need?', 10, 100).get_input()

    if exit_code:
        print('Quantity: %s\nExit Code: %d\n' % (quantity, exit_code))
    else:
        print('Exited')


if __name__ == '__main__':
    main()
