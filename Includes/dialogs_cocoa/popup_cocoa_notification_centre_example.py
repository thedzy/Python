#!/usr/bin/env python3

from popup_cocoa_notification_centre import *


def main():
	# Get input
	notification_msg = Notification("Name", subtitle="First Name", informativeText='Enter your given name', response=True, responseText="Default")
	notification_msg.display()

	AppHelper.runConsoleEventLoop()

	responseCode, responseMessage = notification_msg.getResponse()

	if responseCode == 3:
		print("Response: " + responseMessage)
	else:
		print("User Cancelled")

	# Two option choice
	buttons = ['Go', 'Stop']
	notification_msg = Notification("Warning", subtitle="Functional Error", informativeText='Continue with fake alert', icon='/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/AlertStopIcon.icns', buttons=buttons)
	notification_msg.display()

	AppHelper.runConsoleEventLoop()

	responseCode, responseMessage = notification_msg.getResponse()

	if responseCode == 2:
		print("Button pressed is: " + buttons[0])
	else:
		print("User Cancelled")

	# Multiple options
	buttons = ['Yes', 'No', 'option1', 'option2', 'option3']
	notification_msg = Notification("Select Background", subtitle="3 choices", informativeText='Please choose', contentImage='/System/Library/CoreServices/DefaultBackground.jpg', buttons=buttons)
	notification_msg.display()

	AppHelper.runConsoleEventLoop()

	responseCode, responseMessage = notification_msg.getResponse()

	if responseCode == 4:
		print("Button pressed is: " + str(responseMessage))
	elif responseCode == 4:
		print("Button pressed is: " + str(responseCode))
	else:
		print("User Cancelled")


if __name__ == "__main__":
	main()























