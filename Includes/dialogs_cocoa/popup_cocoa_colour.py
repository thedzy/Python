#!/usr/bin/env python3

"""
Script:	popup_cocoa_colour.py
Date:	2018-11-30

Platform: MacOS

Description:
Creates a GUI colour selection dialog using the PyObjC framework
Returns colour

Currently locks up the NSColorPanel

"""
__author__      = "thedzy"
__copyright__   = "Copyright 2018, thedzy"
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "thedzy"
__email__       = "thedzy@hotmail.com"
__status__      = "Developer"

import os
try:
	import objc
	import Cocoa
	from AppKit import *
	from PyObjCTools import AppHelper
except ImportError as err:
	print(err)
	print("You need to have the PyObjC frameworks installed")
	print("easy_install -U pyobjc")


class ColourDialog(object):

	def __init__(self):

		super(ColourDialog, self).__init__()

	def pick(self, **kwargs):
		dialog = NSColorPanel.alloc().init()
		print("\n".join(dir(NSColorPanel)))

		# Set look
		dialog.setColor_(Cocoa.NSColor.redColor())
		dialog.setShowsAlpha_(True)
		dialog.setMode_(1)
		dialog.setFloatingPanel_(True)
		dialog.setUsingModalAppearance_(True)

		# Set Action
		dialog.setTarget_(self)
		dialog.setAction_("picked:")

		# Set behaviour
		dialog._setModal_(True)
		dialog.setWorksWhenModal_(True)

		dialog.setContinuous_(True)

		#dialog._orderFrontRelativeToWindow_(self)
		dialog.orderFrontRegardless()
		#dialog.orderFront_(None)

		dialog.makeKeyWindow()

		NSApp.activateIgnoringOtherApps_(True)
		AppHelper.runConsoleEventLoop()

	def changeColor_sender(self, sender):
		print("changeColor_sender")

	def picked_(self, sender):
		print("picked")
		print(colour.color)
		AppHelper.stopEventLoop()

	def _focus(self):
		app = NSRunningApplication.runningApplicationWithProcessIdentifier_(os.getpid())
		app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

