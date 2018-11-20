#!/usr/bin/env python3

import os

print ("Paths")

print("Script: " + os.path.realpath(__file__))
print("Path:   " + os.path.dirname(os.path.realpath(__file__)))
print("File:   " + os.path.basename(__file__))
print("Name:   " + os.path.splitext(os.path.basename(__file__))[0])
print("Ext:    " + os.path.splitext(os.path.basename(__file__))[1] + "\n")
