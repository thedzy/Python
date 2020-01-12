#!/usr/bin/env python3

from progress_bar5b import *


def main():
	progressLength = 100

	app = ProgressBar()
	app.setTitle('Progressing...')
	app.setMax(progressLength)
	app.setColour('#cc0000', '#ffffff')
	app.setDeterminante(True)

	for progressCount in range(progressLength):
		time.sleep(.1)  # do real work here
		if app.isActive():
			# Incerement by 1
			app.setIncrement(1)
		print(progressCount)


if __name__ == '__main__':
	main()
