#!/usr/bin/env python3

__author__ = 'Shane Young'
__version__ = '1.0'
__email__ = 'shane.y@nylas.com'
__date__ = '05-04-2022'
__credits__ = ''

__description__ = \
    """
    test_exception.py: 
    Programme description
    """

import argparse
import logging
import json
import pprint

def object_dump(err):
    for attribute in dir(err):
        item = getattr(err, attribute)
        if callable(item):
            print(f'{attribute}()')
        else:
            print(attribute, ':', item)
    logging.error(f'{err.__class__.__name__}: {err}')

# Test exception
try:
    test = json.loads('{"data": "test", "data2": test}')
    pprint.pp(test)

except Exception as err:
    object_dump(err)

