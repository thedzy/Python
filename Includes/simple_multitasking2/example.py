#!/usr/bin/env python3

import time
import random

from simple_multitasking2 import ThreadManager


start_time = time.time()
total_time = 0
threads = []
loops = random.randrange(5, 25)


def random_sleep(index, *args, **kwargs):
    timer_sleep = random.randrange(0, 25)
    time.sleep(timer_sleep)
    return 'Given: {0:3d}, {1:4d}, {2:5d}.  Slept for {3:3d}'.format(index, args[0], kwargs.get('number', None), timer_sleep), timer_sleep

print('Generating 5-25 threads that will take 0-25 seconds to complete')

# Create managing class, with up to 40 concurrent processes
thread_manager = ThreadManager(semaphores=40)

# Create process threads
for x in range(loops):
    thread_manager.append(random_sleep, x, x**2, number=x**3)

# Process all threads
while thread_manager.active_count() > 0:
    for value in thread_manager.getvalues():
        print(value[0])
        total_time += value[1]

print('Total processing time: {0:3d}s'.format(total_time))
print('Actual time :          {0:3.0f}s'.format(time.time() - start_time))
exit()