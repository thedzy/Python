#!/usr/bin/env python3

"""
Script:	download_jss_advancedsearches.py
Date:	2018-10-04

Platform: MacOS

Description:
Downloads the Advanced search criterias.
Data contains a .json for offline searching.
Results are saved in a folder with teh time and date under 'AdvancedSearches'

"""
__author__      = 'thedzy'
__copyright__   = 'Copyright 2018, thedzy'
__license__     = 'GPL'
__version__     = '1.2'
__maintainer__  = 'thedzy'
__email__       = 'thedzy@hotmail.com'
__status__      = 'Developer'


import json
import os
import string
import sys
import time
from io import BytesIO

import pycurl  # #pip3 install pycurl
from popup_userpass import *
from progress_bar5b import *

apiurl = 'https://jamf.example.com/JSSResource'
apiuser = None
apipass = None


def main():
	# Get user credentials through GUI Window
	user_auth()

	fmtdate = time.strftime('%Y.%m.%d.%H.%M.%S')
	object_folder = os.path.dirname(os.path.realpath(__file__)) + '/AdvancedSearches/' + fmtdate
	os.makedirs(object_folder)
	print(object_folder)

	# Create progressbar
	app = ProgressBar()
	app.setColour('#019650', '#ffffff')
	app.setTitle('Reading in Advanced Searches')

	objects = jamf_get_data('advancedcomputersearches')['advanced_computer_searches']
	app.setMax(len(objects))

	# Loop through computergroups
	start_time = time.time()
	for object in objects:

		#print(str(object['id']))
		object_json = jamf_get_data('advancedcomputersearches/id/' + str(object['id']))

		#print(json.dumps(object_json, indent=4, sort_keys=True))
		object_name = object_json['advanced_computer_search']['name']
		del object_json['advanced_computer_search']['computers']

		app.setLabel('%s' % object_name)

		object_data_readable = json.dumps(object_json, indent=4, sort_keys=True)
		#print(object_data_readable)

		object_file = open(object_folder + '/' + format_filename(object_name) + '.' + str(object['id']) + '.json', 'wb')
		object_file.write(object_data_readable.encode())
		object_file.close()

		# Move progress
		app.setIncrement(1)

	# print end/total time
	minutes, seconds = divmod((time.time() - start_time), 60)
	hours, minutes = divmod(minutes, 60)
	print('Time to complete: %02d:%02d:%04.1f' % (hours, minutes, seconds))

def user_auth():
	"""
	Get user credentials
	:return:
	"""
	global apiuser
	global apipass

	apiuser, apipass, exitcode = popupUserPass().getCredentials('JSS Login')

	if exitcode:
		print('Username: %s\nPassword: %s\n' % (apiuser, '********'))
	else:
		print('No credentials supplied')
		exit()

def get_curl(url):
	"""
	Create a standard curl object
	:param url: (string) url
	:return: (Object) Pycurl
	"""
	global apiuser
	global apipass

	curl = pycurl.Curl()

	curl.setopt(pycurl.URL, url)

	# Set Auth
	curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_BASIC)

	# When using user/pss
	curl.setopt(pycurl.USERPWD, '{}:{}'.format(apiuser, apipass))
	curl.setopt(pycurl.HTTPHEADER, ['Accept: application/json', 'Content-Type: application/xml', 'charset=UTF-8'])

	curl.setopt(pycurl.FOLLOWLOCATION, 1)
	curl.setopt(pycurl.NOPROGRESS, 1)
	curl.setopt(pycurl.VERBOSE, 0)

	# Bypass and certificate errors
	curl.setopt(pycurl.SSL_VERIFYPEER, 0)
	curl.setopt(pycurl.SSL_VERIFYHOST, 0)

	# write out to nothing, keep terminal clear
	curl.setopt(pycurl.WRITEFUNCTION, lambda bytes: len(bytes))

	# Set proxies
	# curl.setopt(pycurl.PROXY, 'http://proxy.exmaple.com'')
	# curl.setopt(pycurl.PROXYPORT, 3128)
	# curl.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_HTTP)
	curl.setopt(pycurl.IPRESOLVE, pycurl.IPRESOLVE_V4)

	return curl

def jamf_get_data(object):
	"""
	Get Jamf data passing the URI
	:param object: Object path in jamf
	:return: (json) Object data
	"""
	# Create an empty data set
	jsondata = {}

	apidata = BytesIO()

	# Return on no data requested
	if object is None:
		return jsondata

	# Get accounts
	try:
		# Start Curl
		curl = get_curl(apiurl + '/' + object)

		# write out to to apidata
		curl.setopt(pycurl.WRITEFUNCTION, apidata.write)

		# Perform curl of the page
		curl.perform()

		# Get http code & data
		apicode = curl.getinfo(pycurl.HTTP_CODE)
		#print(apidata.getvalue().decode('utf-8'))

		# Close out pycurl session
		curl.close()

	except pycurl.error:
		#print(apicode)
		apicode = 0

	if apicode == 200:
		#print ('Success getting ' + object)
		jsondata = json.loads(apidata.getvalue())
	else:
		print('HTTP error: ' + str(apicode) + ' at ' + str(get_time()) + ' epoch')
		sys.exit()

	return jsondata

def format_filename(sfilename):
	"""
	Reformat the filename to avoid special characters
	:param sfilename: (String) Filename
	:return: (String) formated filenames
	Note: Borrowed from https://gist.github.com/seanh/93666
	"""
	valid_chars = '-_.() %s%s' % (string.ascii_letters, string.digits)
	filename = ''.join(char for char in sfilename if char in valid_chars)
	filename = filename.replace(' ', '_')  # I don't like spaces in filenames.
	return filename

def get_time():
	"""
	Get epoch time
	:return: (int) Epoch time
	"""
	epochmilli = int(round(time.time() * 1000))
	return epochmilli


if __name__ == '__main__':
	main()

