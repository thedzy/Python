#!/usr/bin/env python3

"""
Script:	popup_cocoa_file.py
Date:	2018-11-30

Platform: MacOS

Description:
Creates a GUI file open/save dialog using the PyObjC framework
Returns filename(s)

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
	from AppKit import *
except:
	print("You need to have the PyObjC frameworks installed")
	print("easy_install -U pyobjc")

class FileDialog(object):

	HOME = os.path.expanduser('~/')

	APPLICATIONS = os.path.expanduser('/Applications/')
	DOWNLOADS = os.path.expanduser('~/Downloads/')
	DOCUMENTS = os.path.expanduser('~/Documents/')
	DESKTOP = os.path.expanduser('~/Desktop/')
	PICTURES = os.path.expanduser('~/Pictures/')
	MOVIES = os.path.expanduser('~/Movies/')

	def __init__(self):

		super(FileDialog, self).__init__()

	def open(self, **kwargs):
		"""
		Creates an Open File dialog window with the keyword parameters specified
		:param kwargs: 
			allowsMultipleSelection (bool): A Boolean that indicates whether the panel’s browser allows the user to open multiple files (and directories) at a time.
			canChooseDirectories (bool): A Boolean that indicates whether the panel allows the user to choose directories to open.
			canChooseFiles (bool): A Boolean that indicates whether the panel allows the user to choose files to open.
			directory (string): A string containing the absolute path of the default directory
			extensionHidden (bool): A Boolean that indicates whether the panel’s browser shows the file extensions of all files and directories
			filetypes (array): The value of this property specifies the file types the user can save the file as. A file type can be a common file extension, or a UTI. The default value of this property is nil, which indicates that any file type can be used.
			message (string): A string containing the message to display to the user above the file selection
			defaultButton (string):  A string containing the text of the "Open" button
			requiredFileType (string): A string containing the required file type ie. "txt"
			resolvesAliases (bool): A Boolean that indicates whether the panel’s browser resolves the alias
			showsHiddenFiles (bool): A Boolean value that indicates whether the panel displays files that are normally hidden from the user.
			title (string): The title of the panel. (non functional)
			treatsFilePackagesAsDirectories (bool):  A Boolean that indicates whether the panel’s browser traverse through packages
		:return (array): File names and paths chosen
		"""
		dialog = NSOpenPanel.alloc().init()

		dialog.setAllowsMultipleSelection_(kwargs.get('allowsMultipleSelection', False))
		dialog.setCanChooseDirectories_(kwargs.get('canChooseDirectories', False))
		dialog.setCanChooseFiles_(kwargs.get('canChooseFiles', True))
		if not kwargs.get('directory', None) is None:
			dialog.setDirectoryURL_(NSURL.fileURLWithPath_(kwargs.get('directory', None)))
		dialog.setExtensionHidden_(kwargs.get('extensionHidden', True))
		if not kwargs.get('message', None) is None:
			dialog.setMessage_(kwargs.get('message', None))
		dialog.setPrompt_(kwargs.get('defaultButton', "Open"))
		if not kwargs.get('requiredFileType', None) is None:
			dialog.setRequiredFileType_(kwargs.get('requiredFileType', None))
		dialog.setResolvesAliases_(kwargs.get('resolvesAliases', True))
		dialog.setShowsHiddenFiles_(kwargs.get('showsHiddenFiles', False))
		dialog.setTitle_(kwargs.get('title', "Open"))
		dialog.setTreatsFilePackagesAsDirectories_(kwargs.get('treatsFilePackagesAsDirectories', False))

		self._focus()
		dialog_return = dialog.runModalForTypes_(kwargs.get('fileTypes', None))
		if dialog_return:
			return dialog.filenames()
		else:
			return ()

	def save(self, **kwargs):
		"""
		Creates an Open Save dialog window with the keyword parameters specified
		:param kwargs:
			allowedFileTypes (array): The value of this property specifies the file types the user can save the file as. A file type can be a common file extension, or a UTI. The default value of this property is nil, which indicates that any file type can be used.
			allowsOtherFileTypes (bool): A Boolean value that indicates whether the panel allows the user to save files with an extension that’s not in the list of allowed types.
			canCreateDirectories (bool): A Boolean value that indicates whether the panel allows the user to create directories.
			directory (string): A string containing the absolute path of the default directory
			extensionHidden (bool): A Boolean value that indicates whether the extension-hiding checkbox is visible and checked.
			message (string): The message text displayed in the save panel.
			nameFieldLabel (string): The string displayed in front of the filename text field.
			nameFieldStringValue (string): A string containing the the default file name
			defaultButton (string): The prompt of the default button.
			requiredFileType (string): Sets the required file type (if any).
			showsHiddenFiles (bool): A Boolean value that indicates whether the panel displays files that are normally hidden from the user.
			showsTagField (bool): A Boolean value that indicates whether the panel displays the Tags field.
			title (string): The title of the panel. (non functional)
			treatsFilePackagesAsDirectories (bool): 
		:return (string): File name and path chosen
		"""
		
		dialog = NSSavePanel.alloc().init()

		if not kwargs.get('allowedFileTypes', ['']) is None:
			dialog.setAllowedFileTypes_(kwargs.get('allowedFileTypes', ['']))
		dialog.setAllowsOtherFileTypes_(kwargs.get('allowsOtherFileTypes', True))
		dialog.setCanCreateDirectories_(kwargs.get('canCreateDirectories', True))
		if not kwargs.get('directory', None) is None:
			dialog.setDirectoryURL_(NSURL.fileURLWithPath_(kwargs.get('directory', None)))
		dialog.setExtensionHidden_(kwargs.get('extensionHidden', True))
		if not kwargs.get('message', None) is None:
			dialog.setMessage_(kwargs.get('message', None))
		dialog.setNameFieldLabel_(kwargs.get('nameFieldLabel', "Save As:"))
		if not kwargs.get('nameFieldStringValue', None) is None:
			dialog.setNameFieldStringValue_(kwargs.get('nameFieldStringValue', None))
		dialog.setPrompt_(kwargs.get('defaultButton', "Save"))
		if not kwargs.get('requiredFileType', None) is None:
			dialog.setRequiredFileType_(kwargs.get('requiredFileType', None))
		dialog.setShowsHiddenFiles_(kwargs.get('showsHiddenFiles', False))
		dialog.setShowsTagField_(kwargs.get('showsTagField', False))
		dialog.setTitle_(kwargs.get('title', "Save"))
		dialog.setTreatsFilePackagesAsDirectories_(kwargs.get('treatsFilePackagesAsDirectories', False))

		self._focus()
		dialog_return = dialog.runModal()
		if dialog_return:
			return dialog.filename()
		else:
			print("\n".join(dir(type(NSURL))))
			return None

	def _focus(self):
		app = NSRunningApplication.runningApplicationWithProcessIdentifier_(os.getpid())
		app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)
