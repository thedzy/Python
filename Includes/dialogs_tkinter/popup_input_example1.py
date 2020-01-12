#!/usr/bin/env python3


from popup_input import *


def main():
	name, exitcode = popupInput().getInput('Name', 'What is your name?')

	if exitcode:
		print('Name: %s\nExit Code: %d\n' % (name, exitcode))
	else:
		print('Exited')


if __name__ == '__main__':
	main()
