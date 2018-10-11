#!/usr/bin/env python3

import os,sys
import time


def main():
	# Enable logging and then print some text
	enable_logging("logs")
	print("Stuff happened")


# Get formatted date
def get_date():
	fmtdate = time.strftime('%Y.%m.%d.%H.%M.%S')
	return fmtdate

# Enable logging of all output
def enable_logging(folder):
	# Set the log path to the string passed (relative path)
	dirname = os.path.dirname(__file__)
	logpath = "/" + folder + "/"
	print("Logging to ", dirname + logpath)

	if not os.path.exists(dirname + logpath):
		os.makedirs(dirname + logpath)

	filename = os.path.join(dirname + logpath + str(get_date()) + ".txt")
	sys.stdout = open(filename, "w+")

	print(time.asctime())


if __name__ == "__main__":
	main()