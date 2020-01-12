#!/usr/bin/env python3

import os
import sys
import time


def main():
	"""
	Enable logging and then print some text
	:return: Void
	"""
	enable_logging('logs')
	print('Stuff happened')

def get_date():
	"""
	Get formatted date
	:return: (String) Formated date
	"""
	fmtdate = time.strftime('%Y.%m.%d.%H.%M.%S')
	return fmtdate

def enable_logging(folder):
	"""
	Enable logging of all output
	:param folder: (String) Path to log folder
	:return: Void
	"""
	# Set the log path to the string passed (relative path)
	dirname = os.path.dirname(__file__)
	logpath = '/' + folder + '/'
	print('Logging to ', dirname + logpath)

	if not os.path.exists(dirname + logpath):
		os.makedirs(dirname + logpath)

	filename = os.path.join(dirname + logpath + str(get_date()) + '.txt')
	sys.stdout = open(filename, 'w+')

	print(time.asctime())


if __name__ == '__main__':
	main()