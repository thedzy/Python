#!/usr/bin/env python3

"""
Script:	popup_cocoa_notification_centre.py
Date:	2018-11-24

Platform: MacOS

Description:
Creates a GUI input notification using the PyObjC framework
Allows for easy access to the notification centre from your python script

"""
__author__      = "thedzy"
__copyright__   = "Copyright 2018, thedzy"
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "thedzy"
__email__       = "thedzy@hotmail.com"
__status__      = "Developer"

try:
	from AppKit import *
	from PyObjCTools import AppHelper
except:
	print("You need to have the PyObjC frameworks installed")
	print("easy_install -U pyobjc")

class Notification(object):
	"""
	Notification (Class)
	Create a message dialog and get user response
	"""

	def __init__(self, messageText, **kwargs):
		"""
		__init__
		Initialise dialog
		:param messageText: "The message for the dialog
		:param kwargs:
			subtitle = Subtitle to title (string)
			informativeText = Information below the alert message (string)
			icon = Path to icon (string)
			buttons = Button texts [ cancelmsg, acceptmsg ] (list, strings)
			response = Whether to use as a response notificatio (bool), overrides buttons
			responseText = Default response text (string)
		"""
		super(Notification, self).__init__()
		self.messageText = messageText
		self.subtitle = kwargs.get('subtitle',"")
		self.informativeText = kwargs.get('informativeText',"")

		self.icon = kwargs.get('icon', None)
		self.contentImage = kwargs.get('contentImage', None)
		self.buttons = kwargs.get('buttons',['OK'])
		self.response = kwargs.get('response', False)
		self.responseText = kwargs.get('responseText', "")

		self.responseCode = 0
		self.responseMessage = ""

	def display(self):
		"""
		Display the message
		:return: NSUserNotification
		"""

		# Initiliase
		notification = NSUserNotification.alloc().init()

		# Set text
		notification.setTitle_(self.messageText)
		notification.setSubtitle_(self.subtitle)
		notification.setInformativeText_(self.informativeText)

		# Set icon
		try:
			if not self.icon is None:
				image = NSImage.alloc().initByReferencingFile_(self.icon)
				notification.set_identityImage_(image)
		except:
			pass


		# Set contentImage (right icon)
		try:
			if not self.contentImage is None:
				image = NSImage.alloc().initByReferencingFile_(self.contentImage)
				notification.setContentImage_(image)
		except:
			pass

		# If the reply option is selected setup the reply, other wise set hte buttons
		if self.response:
			notification.setHasReplyButton_(True)
			notification.setResponsePlaceholder_(self.responseText)
		else:
			if len(self.buttons) > 0:
				notification.setHasActionButton_(True)
				notification.set_showsButtons_(True)
				notification.setActionButtonTitle_(self.buttons[0])
			if len(self.buttons) > 1:
				notification.setOtherButtonTitle_(self.buttons[1])


		# If more than 2 buttons are set, set hte options ans force the appearance
		if len(self.buttons) > 2 and not self.response:
			actions = NSMutableArray.alloc().init()
			for buttonNum in range(2, len(self.buttons)):
				action = NSUserNotificationAction.alloc().init()
				action._setTitle_(self.buttons[buttonNum])
				action._setIdentifier_(self.buttons[buttonNum])
				actions.append(action)

			notification.set_alwaysShowAlternateActionMenu_(True)
			notification.setAdditionalActions_(actions)

		# Sound alert
		notification.setSoundName_('NSUserNotificationDefaultSoundName')

		# Set NSUserNotificationCenter
		center = NSUserNotificationCenter.defaultUserNotificationCenter()
		center.setDelegate_(self)
		center.deliverNotification_(notification)

		return notification

	def userNotificationCenter_didActivateNotification_(self, center, notification):
		"""
		Handle user selections (override)
		:param center: NSUserNotificationCenter
		:param notification: NSUserNotification
		:return:  (void)
		"""
		self.responseCode = notification.activationType()
		self.responseMessage = response = notification.response()

		# If reply option
		if notification.activationType() is 3:
			self.responseMessage = notification.response()

		# In option selection
		if notification.activationType() is 4:
			self.responseMessage = notification.additionalActivationAction().title()

		# Stop even loop if start with runConsoleEventLoop
		AppHelper.stopEventLoop()

	def getResponse(self):
		"""
		Return the stored resoonse of the user c=selection/cancel
		:return:
			responseCode: Event trigger (integer)
			responseMessage: The reply or the user option
		"""
		return self.responseCode, self.responseMessage

	def userNotificationCenter_didDismissAlert_(self, center, notification):
		"""
		Handle the prompt being cancelled by the user
		:param center: NSUserNotificationCenter
		:param notification: NSUserNotification
		:return: Complete (bool)
		"""
		self.responseCode = notification.activationType()
		self.responseMessage = "Cancelled"

		# Stop even loop if start with runConsoleEventLoop
		AppHelper.stopEventLoop()
		return True

	def userNotificationCenter_shouldPresentNotification_(self, center, notification):
		"""
		Handle the prompt never being scheduled to run
		:param center: NSUserNotificationCenter
		:param notification: NSUserNotification
		:return: Complete (bool)
		"""
		# Stop even loop if start with runConsoleEventLoop
		AppHelper.stopEventLoop()
		return True




















