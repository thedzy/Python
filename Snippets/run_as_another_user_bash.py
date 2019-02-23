#!/usr/bin/env python3

import os
import pwd
import subprocess


def main():
	# Use os.getlogin() in place of the username if you want to run a command as the current user
	run_result = run_bash_as_user('whoami', "account")

	if run_result[0] is not None:
		print("Stdout : %s" % run_result[0].decode("utf-8"))
	if run_result[1] is not None:
		print("Stderr : %s" % run_result[1].decode("utf-8"))

	# If you want to seperate the multiline input into an array
	print(run_result[0].decode("utf-8").splitlines())


def run_bash_as_user(cmd, user_name):
	"""
	Runs a command (SH, BASH) as the user passed
	:param cmd: (String) Command to be run (ie. ps -aex | grep sh)
	:param user_name: (String) Username, if user_name is invlaid, it will run as the current user
	:return: (Tupple) stdout and estderr
	"""

	def run_as_user(user_name):
		"""
		Passes a function to set the user, can be used in Popen
		:param user_name: (String) Username
		:return: Function or null if err
		"""
		try:
			pwnam = pwd.getpwnam(user_name)
			user_uid = pwnam.pw_uid
			user_gid = pwnam.pw_gid

			def preexec_fn():
				os.setgid(user_gid)
				os.setuid(user_uid)

			return preexec_fn
		except:
			return None

	cmd_result = subprocess.Popen(cmd, preexec_fn=run_as_user(user_name), shell=True, stdout=subprocess.PIPE,
	                              stderr=subprocess.PIPE).communicate()

	return cmd_result


if __name__ == "__main__":
	main()
