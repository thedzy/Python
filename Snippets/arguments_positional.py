#!/usr/bin/env python3


import sys


# Position 0 is the filename (like bourne shell)
print (sys.argv[0])


# How many parameters where passed
print(len(sys.argv))


# All arguments as one
print (sys.argv)


# Arguments 1 and 3
print ("%s %s" % (sys.argv[1], sys.argv[3]))


# Arguments 4+"
print (sys.argv[4:])


# Arguments 4-6
print (sys.argv[4:7])


# Loop through arguments
for arg in sys.argv:
	print ("Argument:" + arg)
