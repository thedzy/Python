#!/usr/bin/env python3

"""
Script:	download_jss_licensedsoftware.py
Date:	2018-10-04

Platform: MacOS

Description:
Downloads the Licensed Software information.
Data contains a .json for offline searching.
Results are saved in a folder with teh time and date under 'LicensedSoftware'

"""
__author__      = 'thedzy'
__copyright__   = 'Copyright 2018, thedzy'
__license__     = 'GPL'
__version__     = '1.2'
__maintainer__  = 'thedzy'
__email__       = 'thedzy@hotmail.com'
__status__      = 'Developer'


import sys, time, os
import pycurl, urllib.parse # #pip3 install pycurl
import json
from io import BytesIO
import base64
import string

from progress_bar5b import *
from popup_userpass import *

apiurl = 'https://jamf.example.com/JSSResource'
apiuser = None
apipass = None


def main():
	# Get user credentials through GUI Window
	user_auth()

	fmtdate = time.strftime('%Y.%m.%d.%H.%M.%S')
	object_folder = os.path.dirname(os.path.realpath(__file__)) + '/LicensedSoftware/' + fmtdate
	os.makedirs(object_folder)
	print(object_folder)

	# Create progressbar
	app = ProgressBar()
	app.setColour('#019650', '#ffffff')
	app.setTitle('Reading in Licenced Software')

	# Get objects/set progress length
	objects = jamf_get_data('licensedsoftware')['licensed_software']
	app.setMax(len(objects))

	# Loop through objects
	start_time = time.time()
	for object in objects:
		object_json = jamf_get_data('licensedsoftware/id/' + str(object['id']))

		object_name = object_json['licensed_software']['general']['name']

		# Update Status
		app.setLabel('%s' % object_name)

		object_data_readable = json.dumps(object_json, indent=4, sort_keys=True)
		object_file = open(object_folder + '/' + format_filename(object_name) + '.' + str(object['id']) + '.json', 'wb')
		object_file.write(object_data_readable.encode())
		object_file.close()

		# Move progress
		app.setIncrement(1)

	# print end/total time
	minutes, seconds = divmod((time.time() - start_time), 60)
	hours, minutes = divmod(minutes, 60)
	print('Time to complete: %02d:%02d:%04.1f' % (hours, minutes, seconds))


# Get user credentials
def user_auth():
	# Authentication
	global apiuser
	global apipass

	apiuser, apipass, exitcode = popupUserPass().getCredentials('JSS Login')

	if exitcode:
		print('Username: %s\nPassword: %s\n' % (apiuser, '********'))
	else:
		print('No credentials supplied')
		exit()

# Create a standard curl object
def get_curl(url):
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

# Get Jamf data passing the URI
def jamf_get_data(object):
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

# Reformat the filename to avoid special characters
def format_filename(sfilename):
	# Borrowed from https://gist.github.com/seanh/93666
	valid_chars = '-_.() %s%s' % (string.ascii_letters, string.digits)
	filename = ''.join(char for char in sfilename if char in valid_chars)
	filename = filename.replace(' ', '_')  # I don't like spaces in filenames.
	return filename

# Get epoch time
def get_time():
	epochmilli = int(round(time.time() * 1000))
	return epochmilli


if __name__ == '__main__':
	main()

