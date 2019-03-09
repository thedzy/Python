#!/usr/bin/env python3

import time
import os

print("{0:15s}: {1}".format("Created", time.ctime(os.stat(__file__).st_birthtime)))
print("{0:15s}: {1}".format("Last Modified", time.ctime(os.path.getmtime(__file__))))
print("{0:15s}: {1}".format("Last Accessed", time.ctime(os.path.getatime(__file__))))
print("{0:15s}: {1}".format("Last Change", time.ctime(os.path.getctime(__file__))))