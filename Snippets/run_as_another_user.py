#!/usr/bin/env python3

import os
import pwd

def main():
	# Change user context to 'account'
	if change_user_context('account'):
		print("Now running as user %d" % os.getuid())
	else:
		print("Still unning as user %d" % os.getuid())

	# You cannot change back, now you don't have elevated privilages to do so
	if change_user_context('root'):
		print("Now running as user %d" % os.getuid())
	else:
		print("Still unning as user %d" % os.getuid())


def change_user_context(user_name):
	"""
	Change ptyon user context to another user, must be root
	:param user_name: Username
	:return: (Bool) Success
	"""
	pwnam = pwd.getpwnam(user_name)

	try:
		# Only root can change permissions
		if os.getuid() == 0:
			os.setgid(pwnam.pw_gid)
			os.setuid(pwnam.pw_uid)
			return True
		else:
			print("Cannot change to %d Only root can change uid" % pw_uid)
			return False
	except:
		return False


if __name__ == "__main__":
	main()
