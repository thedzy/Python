#!/usr/bin/env python3


from popup_userpass import *
import os


def main():
    username, password, exit_code = PopupUserPass('Login Window', os.getlogin()).get_credentials()

    if exit_code:
        print('Username: %s\nPassword: %s\nExit Code: %d\n' % (username, password, exit_code))
    # After using the username it is best to destroy the variable or reset it's contents
    else:
        print('Exited')


if __name__ == '__main__':
    main()
