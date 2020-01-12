#!/usr/bin/env python3

import sys
import socket


ip = sys.argv[1]

try:
	socket.inet_pton(socket.AF_INET, ip)
	print('Valid IPv4')
except socket.error:
	try:
		socket.inet_pton(socket.AF_INET6, ip)
		print('Valid IPv6')
	except socket.error:
		print('Invalid')
