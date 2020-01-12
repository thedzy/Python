#!/usr/bin/env python3

"""
Script:	pyshell.py
Date:	2019-03-10

Platform: MacOS

Description:
Python functions to simulate bash commands

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2019, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Developer'

import os
import socket
import time


def which(cmd=None):
    success, stderr, stdout = None, None, None
    programmes = []

    for path in os.environ['PATH'].split(os.pathsep):
        if os.path.exists(os.path.join(path, cmd)):
            programmes.append(os.path.join(path, cmd))

    if len(programmes) > 0:
        success = True
        stderr = None
    else:
        success = False
        stderr = 'No programmes found'

    return success, programmes, stderr


def touch(file):
    success, stderr, stdout = None, None, None

    # Check if file has a path
    if not os.path.dirname(file):
        filedir = os.path.dirname(__file__)
        file = '{0}/{1}'.format(filedir, file)
    else:
        filedir = os.path.dirname(file)


    # If path doesnt exist, create it
    if not os.path.isdir(filedir):
        try:
            os.mkfifo(filedir)
        except PermissionError as err:
            success = False
            stderr = '{0}: {1}'.format(filedir, err)
            return success, stdout, stderr
        except OSError as err:
            success = False
            stderr = '{0}: {1}'.format(filedir, err)
            return success, stdout, stderr

    # Touch file
    try:
        with open(file, 'a'):
            os.utime(file, (time.time(), time.time()))
        success = True
        stdout = '{0} touched'.format(file)
    except PermissionError as err:
        success = False
        stderr = '{0}: {1}'.format(file, err)
    except OSError as err:
        success = False
        stderr = '{0}: {1}'.format(file, err)
    finally:
        return success, stdout, stderr


def host(url, **kwargs):
    port = kwargs.get('port', 443)
    timeout = kwargs.get('timeout', socket.getdefaulttimeout())

    # Create a socket to test and then close
    socket_test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socket_test.settimeout(timeout)
        socket_test.connect((url, port))
        return True
    except socket.error as err:
        if err.errno == 61:
            print('Connection Refused')
        socket_test.close()
        return False
    finally:
        socket_test.close()


def ping():
    pass

