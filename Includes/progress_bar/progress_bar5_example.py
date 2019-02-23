#!/usr/bin/env python3

from progress_bar5 import *


def main():
	progressLength = 100

	app = ProgressBar()
	app.setTitle("Progressing...")
	app.setMax(progressLength)
	app.setColour('green', 'white')
	app.setDeterminante(True)

	for progressCount in range(progressLength):
		time.sleep(0.05)  # do real work here
		if app.isActive():
			# Alt: Set the value to progressCount
			#app.setPosition(progressCount)
			# Incerement by 1
			app.setIncrement(1)
		print(progressCount)


if __name__ == "__main__":
	main()
