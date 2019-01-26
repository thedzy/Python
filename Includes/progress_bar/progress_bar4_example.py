#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from progress_bar4 import *

def main():
    prog_length = 33

    for item in range(prog_length):
        time.sleep(0.1) # do real work here
        #progressbar(item + 1, prog_length, "Testing....", [1.0, 1.0, 1.0],[1.0, 0.0, 0.0])
        progressbar(item + 1, prog_length)

    sys.stdout.write("\n")

if __name__ == "__main__":
	main()