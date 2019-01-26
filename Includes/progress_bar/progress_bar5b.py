#!/usr/bin/env python3

"""
Script:	progress_bar5b.py
Date:	2018-09-24

Platform: MacOS

Description:
Creates a GUI progress bar
Customisable colour, title and header
Shows percentage and estimated time,

"""
__author__      = "thedzy"
__copyright__   = "Copyright 2018, thedzy"
__license__     = "GPL"
__version__     = "5.0b"
__maintainer__  = "thedzy"
__email__       = "thedzy@hotmail.com"
__status__      = "Developer"

import tkinter as tk
from tkinter import ttk

import time

class ProgressBar(tk.Tk):
	import time

	"""
	Class to create a visual progresss bar
	Added Esrimated time
	"""

	def __init__(self, *args, **kwargs):
		# Intiliaise as a tkinter class
		tk.Tk.__init__(self, *args, **kwargs)

		self.timestart = time.time()

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
		self.minsize(width=1000, height=70)
		self.maxsize(width=1600, height=70)

		windowcolor='grey90'
		self.configure(background=windowcolor)

		# Set progress bar style
		self.barColour = 'black'
		self.backColour = 'white'
		style = ttk.Style()
		style.theme_use('default')
		style.configure("black.Horizontal.TProgressbar", background='red')
		style.layout("LabeledProgressbar",
         [('LabeledProgressbar.trough',
           {'children': [('LabeledProgressbar.pbar',
                          {'side': 'left', 'sticky': 'ns'}),
                         ("LabeledProgressbar.label",
                          {"sticky": ""})],
           'sticky': 'nswe'})])
		style.configure("LabeledProgressbar", text="0 %", background='green', font=("Helvetica", 16), foregroundforeground="black")

		# Define Lable
		self.labelValue = tk.StringVar(value="Loading...")
		self.label = ttk.Label(self.master, text="xxxxxxxxxxx", justify="left", anchor="w", textvariable=self.labelValue, font=("Helvetica", 16), background=windowcolor)
		self.label.pack(fill=tk.BOTH, expand=True, padx=5)

		# Define Progress bar
		self.progress = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate", style="LabeledProgressbar")
		self.progress.pack(fill=tk.BOTH, expand=True)

		# Define Lable
		self.statusValue = tk.StringVar(value="0.0 seconds")
		self.status = ttk.Label(self.master, text="0.0 seconds", justify="left", anchor="e",
		                       textvariable=self.statusValue, font=("Helvetica", 13), background=windowcolor)
		self.status.pack(fill=tk.BOTH, expand=True, padx=5)

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
		:param max: Integer
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
		''' Increment the bar by a value
		:param increment: integer
		'''
		self.progress.step(increment)

		self.__refresh()

	def setMax(self, max):
		"""
		Set Bar Maximum value
		:param max: Integer
		"""
		self.progress["maximum"] = max

		self.__refresh()

	def setColour(self, barColour='#000000', backColour='#ffffff'):
		"""
		Set the bar foreground and background
		:param barColour: hex starting with #
		:param backColour: hex starting with #
		"""

		# Need a better check
		if barColour.startswith('#') and len(barColour) == 7:
			self.barColour = barColour
		else:
			print("Invalid colour for bar: %s" % barColour)
			self.barColour = "#000000"

		if backColour.startswith('#') and len(backColour) ==7:
			self.backColour = backColour
		else:
			print("Invalid colour for back: %s" % backColour)
			self.barColour = "#000000"

		style = ttk.Style()
		style.configure("LabeledProgressbar", background=self.barColour, troughcolor=self.backColour)

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
		# Calculate time remaining
		timeelapsed = (time.time() - self.timestart)
		try:
			timepredicted = (timeelapsed / self.progress["value"]) * (self.progress["maximum"] - self.progress["value"])
		except:
			timepredicted = 0

		minutes, seconds = divmod(timepredicted, 60)
		hours, minutes = divmod(minutes, 60)
		self.statusValue.set("Estimated Time Remaining: %02d:%02d:%04.1f" % (hours, minutes, seconds))

		# Calculate percent and display
		style = ttk.Style()
		style.configure("LabeledProgressbar", text="%02d%%" % (self.progress["value"]/self.progress["maximum"]*100))

		# Get font colour for overlay text
		style = ttk.Style()
		if (self.progress["value"] / self.progress["maximum"]) > 0.5:
			#print(self._colourContrast(self.barColour))
			if self._colourContrast(self.barColour) < 128:
				txtColour = 'white'
			else:
				txtColour = 'black'
		else:
			#print(self._colourContrast(self.backColour) )
			if self._colourContrast(self.backColour) < 128:
				txtColour = 'white'
			else:
				txtColour = 'black'
		style.configure("LabeledProgressbar", background=self.barColour, troughcolor=self.backColour, foreground=txtColour)

		#print(self._colourContrast(self.barColour))

		# Refresh window
		self.update_idletasks()
		self.update()

	def _colourContrast(self, value):
		# Get style
		#styletest = self.progress["style"]
		#print(ttk.Style().lookup(styletest, 'background'))

		if "name" == "colourname":
			return self._colourContrastName(value)
		if value.startswith('#'):
			return self._colourContrastHex(value)
		if "rgb" == "rgbvalue":
			return self._colourContrastHex(red,green,blue)

		return 0

	def _colourContrastHex(self, hex):
		hex = hex.lstrip('#')
		red, green, blue = tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))
		return self._colourContrastRGB(red, green, blue)

	def _colourContrastName(self, named):
		print("todo: Convert name to rgb, for furutre support")
		return self._colourContrastHex(red, green, blue)

	def _colourContrastRGB(self, red, green, blue):
		# From https://www.w3.org/TR/AERT/#color-contrast
		# Returns 0 - 254
		colourValue = ((red * 299) + (green * 587) + (blue * 114)) / 1000
		return colourValue

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
