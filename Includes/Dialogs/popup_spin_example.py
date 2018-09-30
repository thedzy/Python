#!/usr/bin/env python3


from popup_spin import *


def main():
	quantity, exitcode = popupInput().getInput("Quantity", "How many do you need?", 500)

	if exitcode:
		print("Quantity: %s\nExit Code: %d\n" % (quantity, exitcode))
	else:
		print("Exited")


if __name__ == "__main__":
	main()
