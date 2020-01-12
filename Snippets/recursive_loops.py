#!/usr/bin/env python3

import sys
import os

# Shows the limits of a recursive function
print(sys.getrecursionlimit())

# Shows the limits of a recursive function
sys.setrecursionlimit(1000)


def loop(number):
	"""
	Simple recusrive loop, breaking with an 'if'
	:param number: (Int) loops
	:return:
	"""
	if number < 10:
		number += 1
		return loop(number)
	else:
		return number

print(loop(0))


def exponents(number1, index, number2=1):
	"""
	Simple recusrive loop unsing a while
	:param number1: (int) Number
	:param index: (Int) Exponent
	:param number2: Do not use
	:return: (Int) Value
	"""
	index -= 1
	while index > 0:
		return exponents(number1, index, (number1*number2))
	return number1*number2

print(exponents(9,3))

def dir_struct(path, subpath, index=0):
	"""
	Recursive loop to create directory structure
	:param path: (String) Path to directory
	:param subpath: (String) Directory to recurse
	:param index: Do not use
	:return:
	"""
	items = os.listdir(path + subpath)
	for item in items:
		if os.path.isfile('{0}/{1}/{2}'.format(path, subpath, item)):
			print('\t' * (index + 1) + item)

	for item in items:
		if os.path.isdir('{0}/{1}/{2}/'.format(path, subpath, item)):
			print('\t' * index + item + '/')
			dir_struct('{0}{1}/'.format(path, subpath), item, index+1)


print(os.path.expanduser('~/'), 'Downloads')
dir_struct(os.path.expanduser('~/'), 'Downloads')
