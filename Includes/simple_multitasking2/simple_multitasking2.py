#!/usr/bin/env python3

"""
Script:	simple_multitasking2.py
Date:	2020-01-22
Platform: MacOS
Description:
Class to handle threading, getting its results and tracking if its been handled.
Reduced the complexity and the need for code in your program to use the multi-threading. (as compared to my first version)
https://docs.python.org/3.6/library/threading.html
"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2020, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'


import collections
import threading


class ThreadManager:

    def __init__(self, semaphores=25):
        """
        Initialisation
        """
        self._semaphores = threading.Semaphore(semaphores)

        self._threads = collections.deque()

    def append(self, func, *args, **kwargs):
        """
        Create a new thread by appending it to the threads to be processed
        :param func: (func) Function
        :param args: (list) Arguments
        :param kwargs: (dict) Keywords
        :return: void
        """
        thread = self.ThreadFunction(target=func, args=args, kwargs=kwargs, semaphores=self._semaphores)

        self._threads.append(thread)
        thread.start()

    def set_semaphore(self, semaphores):
        """
        Set the semaphore limit (max concurrent threads)
        :param semaphores:
        :return:
        """
        self._semaphores =threading.Semaphore(semaphores)

    def active_count(self):
        """
        Get remaining thread count
        :return: (int) Threads
        """
        return len(self._threads)

    def getvalues(self):
        """
        Return a list of results of competed threads
        :return: (list)
        """
        current_threads = collections.deque(self._threads)
        complete_thread = collections.deque()
        incomplete_threads = collections.deque()

        while len(current_threads) != 0:
            thread = current_threads.popleft()
            if thread.is_alive():
                incomplete_threads.append(thread)
            else:
                complete_thread.append(thread.value())

        self._threads = incomplete_threads

        return complete_thread


    class ThreadFunction(threading.Thread):

        def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None, semaphores=None):
            """
            Initialisation
            """
            self._semaphores = semaphores
            if 'semaphores' in kwargs:
                del kwargs['semaphores']

            threading.Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)

            self._return = None

        def run(self):
            """
            Override the run to get the return value
            :return:
            """
            self._semaphores.acquire()
            self._return = self._target(*self._args, **self._kwargs)
            return self

        def value(self):
            """
            Get the results of the function
            :return:
            """
            threading.Thread.join(self)
            self._semaphores.release()
            return self._return
