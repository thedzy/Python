#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from progress_bar3 import *


def main():
	prog_length = 33

	for item in range(prog_length):
		# do real work here
		time.sleep(0.1)
		progressbar(item + 1, prog_length, ' Loading....', [1.0, 0.1, 0.5])

	print()

if __name__ == '__main__':
	main()
