#!/usr/bin/env python3


from pyshell import *

# which
print('cmd: {0:20s}Return: {1}'.format('which', which('echo')))


# host
print('cmd: {0:20s}Return: {1}'.format('host', host('google.com')))