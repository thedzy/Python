#!/usr/bin/env python3

from popup_cocoa_dialog import *


def main():
	buttons = ['Cancel', 'Yes', 'No']
	alert_msg = Alert('Alert Message',
	                  informativeText='Information about the alert and what do or choose',
	                  icon='/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/AlertStopIcon.icns',
	                  buttons=buttons,
	                  style=Alert.INFORMATIONAL)
	print('You pressed: ' + buttons[alert_msg.display()])


if __name__ == '__main__':
	main()
