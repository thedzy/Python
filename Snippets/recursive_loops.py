#!/usr/bin/env python3

import sys
import os

# Shows the limits of a recursive function
print(sys.getrecursionlimit())

# Shows the limits of a recursive function
sys.setrecursionlimit(1000)

# Simple recusrive loop, breaking with an "if"
def loop(number):
	if number < 10:
		number += 1
		return loop(number)
	else:
		return number

print(loop(0))


# Simple recusrive loop unsing a while
def exponents(number1, index, number2=1):
	index -= 1
	while index > 0:
		return exponents(number1, index, (number1*number2))
	return (number1*number2)

print(exponents(9,3))

# Recursive loop to create directory structure
def dir_struct(path, subpath, index=0):

	items = os.listdir(path + subpath)

	for item in items:
		if os.path.isfile("{0}/{1}/{2}".format(path, subpath, item)):
			print("\t" * (index + 1) + item )

	for item in items:
		if os.path.isdir("{0}/{1}/{2}/".format(path, subpath, item)):
			print("\t" * index + item + "/")
			dir_struct("{0}{1}/".format(path, subpath), item, index+1)

print(os.path.expanduser('~/'), 'Downloads')
dir_struct(os.path.expanduser('~/'), 'Downloads')