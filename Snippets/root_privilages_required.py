#!/usr/bin/env python3

import os
import sys

if os.geteuid() == 0:
    print("Running as root!")
else:
    # We are not root, restart as root
    os.execvp("sudo", ["sudo"] + sys.argv)

print("Do something")
