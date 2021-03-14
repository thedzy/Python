#!/usr/bin/env python3


from popup_textbox import *


def main():
    answer, exit_code = PopupText('Essay', 'Please describe yourself', 'Vitals:\nName: \nAddress:\n').get_input()

    if exit_code:
        print('Text: %s\nExit Code: %d\n' % (answer, exit_code))
    else:
        print('Exited')


if __name__ == '__main__':
    main()
