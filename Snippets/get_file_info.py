#!/usr/bin/env python3

import os
import time

file_stats = os.stat("get_file_info.py")

print("mode  = {0}".format(oct(file_stats[0])[-4:]))
print("ino   = {0}".format(file_stats[1]))
print("dev   = {0}".format(file_stats[2]))
print("nlink = {0} links".format(file_stats[3]))
print("uid   = {0}".format(file_stats[4]))
print("gid   = {0}".format(file_stats[5]))
print("size  = {0:0.2f}kb".format(file_stats[6] / 1024))
print("atime = {0}".format(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(file_stats[7]))))
print("mtime = {0}".format(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(file_stats[8]))))
print("ctime = {0}".format(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(file_stats[9]))))
