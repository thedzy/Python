#!/usr/bin/env python3


from popup_input import *


def main():
    shared_secret, exit_code = PopupInput('Passphrase', 'What is the passphrase?', True).get_input()

    if exit_code:
        print('Passphrase: %s\nExit Code: %d\n' % (shared_secret, exit_code))
    else:
        print('Exited')


if __name__ == '__main__':
    main()
