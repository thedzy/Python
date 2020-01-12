#!/usr/bin/env python3

import optparse

# Create the parser and give it the program version #
parser = optparse.OptionParser(version='%prog 1.0')

# Store an option
parser.add_option('-o', '--outfile',
                  action='store', dest='outfile', default='/tmp/outfile/txt',
                  help='OutFile: The file that will be created')
# Store multiple infiles
parser.add_option('-i', '--infile',
                  action='append', dest='infiles',
                  help='InFile: The files that will read the create the result')
# Store True if seen
parser.add_option('-c', '--colour',
                  action='store_false', dest='colour', default=True,
                  help='Colour output, not compatible with -b')
# Store False if seen
parser.add_option('-b', '--black',
                  action='store_true', dest='black', default=False,
                  help='Black output, not compatible with -c')
# Store how many times the option is chosen
parser.add_option('-v', '--verbose',
                  action='count', dest='verbose',
                  help='More v's more verbose')
options, args = parser.parse_args()

if not options.colour:
	print('Colour      : False')
else:
	print('Colour      : True')

if options.black:
	print('Black       : True')
else:
	print('Black       : False')

if options.verbose == 0:
	print('Debug level : Off')
elif options.verbose == 1:
	print('Debug level : %s ' % options.verbose)
elif options.verbose == 2:
	print('Debug level : %s ' % options.verbose)
else:
	print('Debug level : Max')

if options.infiles:
	print('InFiles     :')
	for infile in options.infiles:
		print('              %s' % infile)
else:
	print('InFile      : None')

print('Outfile     : %s' % options.outfile)
