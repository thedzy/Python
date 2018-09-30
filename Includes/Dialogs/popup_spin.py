#!/usr/bin/env python3

"""
Script:	popup_spin.py
Date:	2018-09-30

Platform: MacOS

Description:
Creates a GUI spinner to select a number

"""
__author__      = "thedzy"
__copyright__   = "Copyright 2018, thedzy"
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "thedzy"
__email__       = "thedzy@hotmail.com"
__status__      = "Developer"


import sys, os
import tkinter as tk
from tkinter import ttk


class popupInput(tk.Tk):
	"""
	Class to create a vusername password dialog
	"""

	def __init__(self, *args, **kwargs):
		# Intiliaise as a tkinter class
		tk.Tk.__init__(self, *args, **kwargs)

		# Initisalise the draw
		self.createWindow()

		# Button Handlers
		self.protocol("WM_DELETE_WINDOW", self.close)
		self.bind('<Return>', lambda event: self.buttonOK())

	def createWindow(self):

		# Upper center window
		x = (self.winfo_screenwidth() / 2) - 100
		y = (self.winfo_screenheight() / 3) - 45
		self.geometry("+%d+%d" % (x, y))

		# Set min/max sizing for resizing
		self.minsize(width=400, height=130)
		self.maxsize(width=2400, height=130)

		windowcolor = 'grey90'
		self.configure(background=windowcolor)

		# Frame 1
		self.frame1 = tk.Frame(self, background=windowcolor)
		self.inputlabelValue = tk.StringVar(value="Input:")
		self.inputlabel = ttk.Label(self.frame1,  textvariable=self.inputlabelValue, justify="left", anchor="w", font=("Helvetica", 16), width=10, background=windowcolor)
		self.inputlabel.pack(fill=tk.X, expand=True)

		self.frame1.pack(fill=tk.X, expand=True, padx=5, pady=5)

		# Frame 2
		self.frame2 = tk.Frame(self, background=windowcolor)
		self.input = tk.StringVar()
		self.inputfield = tk.Spinbox(self.master, textvariable=self.input, from_=0, to=100, font=("Helvetica", 16),background="white")
		self.inputfield.pack(fill=tk.X, expand=True)

		self.frame2.pack(fill=tk.X, expand=True, padx=5)

		# Frame 3
		self.frame3 = tk.Frame(self, background=windowcolor)
		self.button2 = tk.Button(self.frame3, text='Cancel', justify="center", anchor="ne", highlightbackground=windowcolor, command=self.buttonCancel)
		self.button2.pack(side=tk.RIGHT)

		self.button1 = tk.Button(self.frame3, text='OK', justify="center", anchor="ne", highlightbackground=windowcolor, command=self.buttonOK)
		self.button1.pack(side=tk.RIGHT)
		self.frame3.pack(fill=tk.X, expand=True, padx=5)

		# Try to set window focus
		try:
			from Cocoa import NSRunningApplication, NSApplicationActivateIgnoringOtherApps
		except:
			print ("pip3 install pyobjc")
			sys.exit()
		app = NSRunningApplication.runningApplicationWithProcessIdentifier_(os.getpid())
		app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

	def buttonOK(self):
		self.exitcode = True
		self.close()

	def buttonCancel(self):
		self.exitcode = False
		self.close()

	def setTitle(self, title):
		# Set title of Window and label
		self.title(title)

	def close(self):
		# Detroy the window and mark and inactive
		self.destroy()

	def getInput(self, title="Scale", question="Please input:", max=100):
		# Hide input
		self.setTitle(title)
		self.inputlabelValue.set(question)
		self.wm_deiconify()
		self.inputfield.focus_force()
		self.wait_window()
		return self.input.get(), self.exitcode
