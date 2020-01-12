#!/usr/bin/env python3

"""
Script:	download_jss_scripts.py
Date:	2018-10-04

Platform: MacOS

Description:
Downloads the scripts information.
Data contains a .sh and .json for offline searching.
Results are saved in a folder with teh time and date under 'Scripts'

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
	script_folder = os.path.dirname(os.path.realpath(__file__)) + '/Scripts/' + fmtdate
	os.makedirs(script_folder)
	print(script_folder)

	# Get collection iformation
	scripts = jamf_get_data('scripts')['scripts']

	# Create progressbar
	app = ProgressBar()
	app.setColour('#019650', '#ffffff')
	app.setTitle('Reading in Groups')

	# Loop through scripts
	start_time = time.time()
	for script in scripts:
		script_json = jamf_get_data('scripts/id/' + str(script['id']))
		script_data = script_json['script']['script_contents_encoded']

		script_name = script_json['script']['name']

		# Clean the script out of the json
		del script_json['script']['script_contents_encoded']
		del script_json['script']['script_contents']

		# Update Status
		app.setLabel('%s' % script_name)

		# Write out files 1 script, 1 json of accompanying data
		script_json_readable = json.dumps(script_json, indent=4, sort_keys=True)
		script_json_file = open(script_folder + '/' + format_filename(script_name) + '.' + str(script['id']) + '.json', 'wb')
		script_json_file.write(script_json_readable.encode())
		script_json_file.close()

		script_file = open(script_folder + '/' + format_filename(script_name) + '.' + str(script['id']) + '.sh', 'wb')
		script_file.write(base64.standard_b64decode(script_data))
		script_file.close()

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

	return jsondata

# Reformat filename for special characters
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

