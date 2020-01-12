#!/usr/bin/env python3

try:
	# Will fail:
	os.mkdir('/tmp/path/does/not exist')
except:
	print('Performing error correction\n')
finally:
	print('Do this regardless')

try:
	# Will succeed
	os.makedirs('/tmp/path/does/not exist')
except:
	print('Performing error correction\n')
finally:
	print('Do this regardless')
