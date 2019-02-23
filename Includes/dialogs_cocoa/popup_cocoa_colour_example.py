#!/usr/bin/env python3

from popup_cocoa_colour import *


def main():
	dialog = ColourDialog()
	colour = dialog.pick()

	print(colour)


if __name__ == "__main__":
	main()
