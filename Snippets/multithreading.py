#!/usr/bin/env python3

import threading
import time
import random

start_time = time.time()
total_time = 0
loops = random.randrange(5, 25)

print("Generating 5-25 threads that will take 0-25 seconds to complete")


def random_sleep(index, *args, **kwargs):
	timer_sleep = random.randrange(0, 25)
	time.sleep(timer_sleep)
	print('Given: {0:2d}, {1:3d}, {2:4d}.  Slept for {3:2d}'.format(index, args[0], kwargs.get('number', None), timer_sleep))


for x in range(loops):
	thread = threading.Thread(group=None, target=random_sleep, name=None, args=[x, x**2], kwargs={"number": x**3}, daemon=None)
	thread.start()

# Will wait for the last thread
thread.join()

print("Actual time :  {0:3.0f}s".format(time.time() - start_time))
