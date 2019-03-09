#!/usr/bin/env python3

import os
from SystemConfiguration import *
from Foundation import NSMutableDictionary

if os.getuid() != 0:
    print('WARNING: Not running as root')

# Initiates access to the per-system set of configuration preferences.
prefs = SCPreferencesCreate(None, os.path.splitext(os.path.basename(__file__))[0], None)
# Returns the dictionary associated with NetworkServices
networks_services = SCPreferencesPathGetValue(prefs,'/NetworkServices')

# Create dictionary if missing
if not networks_services:
    print('Failed to load dictionary of NetworkServices')
    exit(3)

# For each network service apply/set ProxyAutoDiscoveryEnable
for networks_service in networks_services:
    user_defined_name = networks_services[networks_service]['UserDefinedName']
    networks_services[networks_service]['Proxies']['ProxyAutoDiscoveryEnable'] = 1
    if SCPreferencesPathSetValue(prefs, '/NetworkServices/{0}/Proxies'.format(networks_service), networks_services[networks_service]['Proxies']):
        print('Configuration for: {} is changed'.format(user_defined_name))
    else:
        print('Error changing configuration for: {}'.format(user_defined_name))

# Check that configuration applied
if not prefs:
    exit()
if not SCPreferencesCommitChanges(prefs):
    print('Failed to Commit Changes')
    exit(1)
if not SCPreferencesApplyChanges(prefs):
    print('SFailed to Apply Changes')
    exit(2)