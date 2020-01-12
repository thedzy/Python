#!/usr/bin/env python3


from popup_input import *


def main():
	sharedsecret, exitcode = popupInput().getInput('Passphrase', 'What is the passphrase?', True)

	if exitcode:
		print('Passphrase: %s\nExit Code: %d\n' % (sharedsecret, exitcode))
	else:
		print('Exited')


if __name__ == '__main__':
	main()
