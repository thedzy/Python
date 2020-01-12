#!/usr/bin/env python3

import time
import random

from simple_multitasking import *


start_time = time.time()
total_time = 0
threads = []
loops = random.randrange(5, 25)


def random_sleep(index, *args, **kwargs):
	timer_sleep = random.randrange(0, 25)
	time.sleep(timer_sleep)
	return 'Given: {0:2d}, {1:3d}, {2:4d}.  Slept for {3:2d}'.format(index, args[0], kwargs.get('number', None), timer_sleep)


print('Generating 5-25 threads that will take 0-25 seconds to complete')

# Create process threads
for x in range(loops):
	threads.append(ThreadFunction(random_sleep, x, x**2, number=x**3))
	threads[len(threads) - 1].start()

# Process in order or by first completed
# Assuming no post processing is required, each takes the same time
process_in_order = False
if process_in_order:
	print('Processing in order, notice the given values increment')
	for thread in threads:
		print(thread.getValue())
		total_time += thread.getTime()
else:
	print('Processing by first complete, notice the sleep values increment')
	unhandled_threads = [t for t in threads if not t.isHandled()]
	while len(unhandled_threads) != 0:
		# Loop through processed threads
		for unactive_thread in [a for a in unhandled_threads if not a.isAlive()]:
			print(unactive_thread.getValue())
			total_time += unactive_thread.getTime()
		unhandled_threads = [t for t in threads if not t.isHandled()]

print('Total processing time: {0:3d}s'.format(total_time))
print('Actual time :          {0:3.0f}s'.format(time.time() - start_time))
exit()
