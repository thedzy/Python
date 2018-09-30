#!/usr/bin/env python3


from popup_userpass import *


def main():
	username, password, exitcode = popupUserPass().getCredentials("JSS Login")

	if exitcode:
		print("Username: %s\nPassword: %s\nExit Code: %d\n" % (username, password, exitcode))
	else:
		print("Exited")


if __name__ == "__main__":
	main()
