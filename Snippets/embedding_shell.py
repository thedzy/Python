#!/usr/bin/env python3

import os
import subprocess

command = '/usr/sbin/system_profiler SPHardwareDataType | /usr/bin/awk '/Serial/ {print $4}''

"""
Using os.system
Pros: Simple, quick
Cons: Does not return output
"""
returncode = os.system(command)
if returncode == 0:
	print('Success\n')

"""
Using subprocess.run
Pros: Returns stdout, stderr, return code
Cons: More complicated
"""
processinfo = subprocess.run(command,
                             shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
print(processinfo.stdout)
if processinfo.returncode == 0:
	print('Success\n')
else:
	print('stderr: ' + processinfo.stderr)

"""
Using subprocess.Popen
Pros: More comtrol over the process(s)
Cons: More complicated
"""
process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output = process.communicate()
if process.returncode == 0:
	print(output[0].decode('utf-8'))
else:
	print(output[1].decode('utf-8'))
