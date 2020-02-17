#!/usr/bin/env python3

import time
import random

from simple_multitasking2 import ThreadManager


start_time = time.time()
total_time = 0
loops = random.randrange(5, 25)

# Let's create a function to spend time
def random_sleep(index, *args, **kwargs):
    timer_sleep = random.randrange(0, 25)
    time.sleep(timer_sleep)
    return '| {0:^10d} | {1:^10d} | {2:^10d} | {3:^10d} |'.format(index, args[0], kwargs.get('number', None), timer_sleep), timer_sleep

# Create managing class, with up to 40 concurrent processes
thread_manager = ThreadManager(semaphores=40)

# Create process threads
for x in range(loops):
    # Append the function to the queue.
    # Function: random_sleep
    # Positional parameters: x
    # Arguments: x**2
    # Named Arguments: number=x**3
    thread_manager.append(random_sleep, x, x**2, number=x**3)

# Print a header to our table
print('Generating 5-25 threads that will take 0-25 seconds to complete')
print('{1}{0}{1}{0}{1}{0}{1}{0}{1}'.format('-' * 12, '+'))

print('| {0:<10s} | {1:<10s} | {2:<10s} | {3:<10s} |'.format('Positional', 'First', 'Named', 'Sleep'))
print('| {0:<10s} | {1:<10s} | {2:<10s} | {3:<10s} |'.format('Argument', 'Argument', 'Argument', 'Time'))
print('{1}{0}{1}{0}{1}{0}{1}{0}{1}'.format('-' * 12, '+'))

# Process all threads
# While the queue is noot empty
while thread_manager.active_count() > 0:
    # Loop through completed processes and get the return value
    for value in thread_manager.getvalues():
        # Print the first returned valuesr and add up the time (second returned) that was spent in all the processes
        print(value[0])
        total_time += value[1]

# Print a footer to our table
# Print processing time (time that would otherwise have been spent if done sequentially) and time taken
print('{1}{0}{1}{0}{1}{0}{1}{0}{1}'.format('-' * 12, '+'))
print('  {0:^10s} | {1:>23s} | {2:^10d} |'.format('', 'Total Processing Time', total_time))
print('  {0:^10s} | {1:>23s} | {2:^10.0f} |'.format('', 'Actual Time', time.time() - start_time))
print('  {0:^10s} +{1}+{2}+'.format('', '-' * 25, '-' * 12))



exit()
