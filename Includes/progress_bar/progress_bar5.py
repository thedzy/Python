#!/usr/bin/env python3

"""
Script:	progress_bar5.py
Date:	2018-09-24

Platform: MacOS

Description:
Creates a GUI progress bar
Customisable colour, title and header

"""
__author__      = "thedzy"
__copyright__   = "Copyright 2018, thedzy"
__license__     = "GPL"
__version__     = "5.0"
__maintainer__  = "thedzy"
__email__       = "thedzy@hotmail.com"
__status__      = "Developer"

import tkinter as tk
from tkinter import ttk


class ProgressBar(tk.Tk):
	"""
	Class to create a visual progresss bar
	"""

	def __init__(self, *args, **kwargs):
		# Intiliaise as a tkinter class
		tk.Tk.__init__(self, *args, **kwargs)

		# Initisalise the draw
		self.createWindow()

		# Refresh the window
		self.__refresh()

		# Flag app as active, tracking a close
		self.active = True

		# Destroy the window is the app is closed
		self.protocol("WM_DELETE_WINDOW", self.close)

	def createWindow(self):
		# Set min/max sizing for resizing
		self.minsize(width=200, height=50)
		self.maxsize(width=1600, height=50)

		windowcolor = 'grey90'
		self.configure(background=windowcolor)

		# Set progress bar style
		style = ttk.Style()
		style.theme_use('default')
		style.configure("black.Horizontal.TProgressbar", background='red')

		# Define Lable
		self.labelValue = tk.StringVar(value="Loading...")
		self.label = ttk.Label(self.master, text="xxxxxxxxxxx", justify="left", anchor="w", textvariable=self.labelValue, font=("Helvetica", 16), background=windowcolor)
		self.label.pack(fill=tk.BOTH, expand=True, padx=5)

		# Define Progress bar
		self.progress = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
		self.progress.pack(fill=tk.BOTH, expand=True)

		# Initialise positions
		self.setMax(100)
		self.setPosition(0)

	def setTitle(self, title):
		# Set title of Window and label
		self.title(title)

		self.__refresh()

	def setLabel(self, title):
		# Set title of Window and label
		self.labelValue.set(title)

		self.__refresh()

	def setPosition(self, position):
		"""
		Set Bar position value
		:param position: Integer
		"""
		self.progress["value"] = position

		self.__refresh()

	def getPosition(self):
		"""
		Get Position
		:return: Interger
		"""
		return self.progress["value"]

	def setIncrement(self, increment):
		""" Increment the bar by a value
		:param increment: integer
		"""
		self.progress.step(increment)

		self.__refresh()

	def setMax(self, max):
		"""
		Set Bar Maximum value
		:param max: Integer
		"""
		self.progress["maximum"] = max

		self.__refresh()

	def setColour(self, barColour='black', backColour='grey'):
		"""
		Set the bar foreground and background
		:param barColour: black', 'yellow', 'white', 'green', 'grey', 'red', 'blue', 'orange', 'grey45'
		:param backColour: black', 'yellow', 'white', 'green', 'grey', 'red', 'blue', 'orange', 'grey45'
		"""
		style = ttk.Style()
		style.theme_use('default')
		style.configure("Horizontal.TProgressbar", background=barColour, troughcolor=backColour)

		self.__refresh()

	def setDeterminante(self, bool=True):
		"""
		Toggle the style from determinate to indeterminate
		:param bool: Bool, true=determinate
		"""
		style = ttk.Style()
		style.theme_use('default')
		if bool:
			style.configure("Horizontal.TProgressbar", mode="determinate")
		else:
			style.configure("Horizontal.TProgressbar", mode="indeterminate")

		self.__refresh()

	def __refresh(self):
		# Refresh window
		self.update_idletasks()
		self.update()

	def close(self):
		# Detroy the window and mark and inactive
		self.destroy()
		self.active = False

	def isActive(self):
		"""
		Return whether the window is inactive to prevent errors in calling for updates
		:return: bool
		"""
		return self.active
