#!/usr/bin/env python3

from progress_bar6 import *


def main():
	progressLength = 100

	app = ProgressBar()
	app.setTitle('Progressing...')
	app.setMax(progressLength)
	app.setColour('#00aa00', '#ffffff')
	app.setDeterminante(True)

	for progressCount in range(progressLength):
		time.sleep(.1)  # do real work here
		if app.isActive():
			# Incerement by 1
			app.setIncrement(1)
			app.setLabel('Loading... {0}'.format(progressCount))
		app.addOutput(str(progressCount) + '\n -- ')


if __name__ == '__main__':
	main()
