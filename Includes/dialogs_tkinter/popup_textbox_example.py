#!/usr/bin/env python3


from popup_textbox import *


def main():
	answer, exitcode = popupInput().getInput("Essay", "Please describe yourself")

	if exitcode:
		print("Text: %s\nExit Code: %d\n" % (answer, exitcode))
	else:
		print("Exited")


if __name__ == "__main__":
	main()
