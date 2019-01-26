#!/usr/bin/env python


"""
Script:	popup_cocoa_notification_centre.py
Date:	2019-01-26

Platform: MacOS

Description:
Send an Apple Event to an application or the login window

Lots of help from:
https://gist.github.com/pudquick/9683c333e73a82379b8e377eb2e6fc41

"""
__author__      = "thedzy"
__copyright__   = "Copyright 2019, thedzy"
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "thedzy"
__email__       = "thedzy@hotmail.com"
__status__      = "Developer"


import struct
import objc
from Foundation import NSBundle
from Cocoa import NSAppleEventDescriptor


objc.loadBundleFunctions(NSBundle.bundleWithIdentifier_('com.apple.AE'),
                         globals(),
                         [("AESendMessage", b"i^{AEDesc=I^^{OpaqueAEDataStorageType}}^{AEDesc=I^^{OpaqueAEDataStorageType}}iq"), ])


def send_apple_event(event, app='com.apple.loginwindow'):
	"""
	Send an event code to an application
	:param event: (String) Event code
		Examples:
		kAELogOut               = logo
		kAEReallyLogOut         = rlgo
		kAEShowRestartDialog    = rrst
		kAEShowShutdownDialog   = rsdn
		kAESleep                = slep
		kAEWakeUpEvent          = wake
		kAEShutDown             = shut
		kAEQuitAll              = quia
		kAERestart              = rest
		See: https://github.com/chrisjenx/wakemesleepme/blob/master/OSX/CoreServices.framework/Versions/A/Frameworks/AE.framework/Versions/A/Headers/AERegistry.h
	:param app: BundleID, default=com.apple.loginwindow
		Use: mdls -name kMDItemCFBundleIdentifier -r /path/to/application.app
	:return:
	"""

	AETimeout = {
		'kAEDefaultTimeout'          :    -1,  # timeout value determined by AEM
		'kNoTimeOut'                 :    -2   # wait until reply comes back, however long it takes
	}

	AESendMode = {
		'kAENoReply'                 :     1,  # sender doesn't want a reply to event
		'kAEQueueReply'              :     2,  # sender wants a reply but won't wait
		'kAEWaitReply'               :     3,  # sender wants a reply and will wait
		'kAEDontReconnect'           :   128,  # don't reconnect if there is a sessClosedErr from PPCToolbox
		'kAEWantReceipt'             :   512,  # (nReturnReceipt) sender wants a receipt of message
		'kAENeverInteract'           :    16,  # server should not interact with user
		'kAECanInteract'             :    32,  # server may try to interact with user
		'kAEAlwaysInteract'          :    48,  # server should always interact with user where appropriate
		'kAECanSwitchLayer'          :    64,  # interaction may switch layer
		'kAEDontRecord'              :  4096,  # don't record this event - available only in vers 1.0.1 and greater
		'kAEDontExecute'             :  8192,  # don't send the event for recording - available only in vers 1.0.1 and greater
		'kAEProcessNonReplyEvents'   : 32768,  # allow processing of non-reply events while awaiting synchronous AppleEvent reply
		'kAEDoNotAutomaticallyAddAnnotationsToEvent': 0x00010000 # if set, don't automatically add any sandbox or other annotations to the event
	}

	# https://developer.apple.com/documentation/coreservices/apple_events/1542799-id_constants_for_the_aecreateapp
	AECreateAppleEvent = {
		"kAutoGenerateReturnID"      :    -1,  # the Apple Event Manager assigns to the created Apple event a return ID that is unique to the current session
		"kAnyTransactionID"          :     0   # if the Apple event is not one of a series of interdependent Apple events
	}

	# Targeting applications by bundle ID is only available in Mac OS X 10.3 or later.
	event_descriptor = NSAppleEventDescriptor.alloc().initWithDescriptorType_data_(FOUR_CHAR_CODE('bund'), buffer(app))

	# build an event descriptor with our app descriptor as the target and the kAELogOut eventID
	event = NSAppleEventDescriptor.appleEventWithEventClass_eventID_targetDescriptor_returnID_transactionID_(
		FOUR_CHAR_CODE('aevt'),
		FOUR_CHAR_CODE(event),
		event_descriptor,
		AECreateAppleEvent["kAutoGenerateReturnID"],
		AECreateAppleEvent["kAnyTransactionID"]).aeDesc()

	# http://mirror.informatimago.com/next/developer.apple.com/documentation/Carbon/Reference/Apple_Event_Manager/apple_event_manager.pdf
	return AESendMessage(event, None, AESendMode["kAENoReply"] | AESendMode["kAENeverInteract"], AETimeout["kAEDefaultTimeout"])


def FOUR_CHAR_CODE(code):
	"""
	Convert a four-char-code to the correct 8-bit value
	:return: (Integer)
	"""
	return struct.unpack('>L', code)[0]
