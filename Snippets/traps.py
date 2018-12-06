#!/usr/bin/env python3

import atexit


@atexit.register
def trap_exit():
	print("Do necessary clean up")


print("Do stuff")
exit()
