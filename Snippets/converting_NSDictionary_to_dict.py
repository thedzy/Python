#!/usr/bin/env python3

import json
from SystemConfiguration import *
from Foundation import __NSCFDictionary
from Foundation import __NSCFArray

def convert_to_dict(old_dict, new_dict):
    if isinstance(old_dict, __NSCFDictionary):
        try:
            for key in old_dict:
                if isinstance(old_dict[key], objc.pyobjc_unicode) or isinstance(old_dict[key], objc._pythonify.OC_PythonLong):
                    new_dict[key] = old_dict[key]
                elif isinstance(old_dict[key], __NSCFArray):
                    new_dict[key] = []
                    convert_to_dict(old_dict[key], new_dict[key])
                else:
                    new_dict[key] = {}
                    convert_to_dict(old_dict[key], new_dict[key])
        except:
            return

    if isinstance(new_dict, list):
        for key in old_dict:
            if isinstance(key, objc.pyobjc_unicode) or isinstance(key, objc._pythonify.OC_PythonLong):
                new_dict.append(key)
            elif isinstance(key, __NSCFArray):
                new_array = []
                new_dict.append(new_array)
                convert_to_dict(old_dict[key], new_array)
            elif isinstance(key, __NSCFDictionary):
                new_dict[key] = {}
                convert_to_dict(old_dict[key], new_dict[key])





prefs = SCPreferencesCreate(None, "", None)
network = SCPreferencesPathGetValue(prefs,'/NetworkServices')

print('Before')
print("=" * 40)
print(network)
print("=" * 40)


print('After')
print("=" * 40)
new_dict = {}
convert_to_dict(network, new_dict)
print(json.dumps(new_dict, indent=4))
print("=" * 40)