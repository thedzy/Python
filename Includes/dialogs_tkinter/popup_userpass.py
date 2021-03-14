#!/usr/bin/env python3

"""
Script:	popup_userpass.py
Date:	2018-09-30

Platform: MacOS/Windows

Description:
Creates a GUI input dialog for username and password

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2018, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'

import os
import tkinter as tk
from tkinter import ttk

try:
    from Cocoa import NSRunningApplication, NSApplicationActivateIgnoringOtherApps
except ImportError as err:
    print('Install pyobjc to bring to front')


class PopupUserPass(tk.Tk):
    """
    Class to create a username password dialog
    """

    def __init__(self, title='Login', username='', *args, **kwargs):
        # Initialise as a tkinter class
        tk.Tk.__init__(self, *args, **kwargs)

        # Initialise the draw
        self.__create_window()

        # Default exit code
        self.exit_code = False

        # Setup window
        self.set_title(title)
        self.set_username(username)

        # Button Handlers
        self.protocol('WM_DELETE_WINDOW', self.__close)
        self.bind('<Return>', lambda event: self.__event_button_ok())

    def __create_window(self):

        # Upper center window
        x = (self.winfo_screenwidth() / 2) - 100
        y = (self.winfo_screenheight() / 3) - 45
        self.geometry('+%d+%d' % (x, y))

        # Set min/max sizing for resizing
        self.minsize(width=200, height=105)
        self.maxsize(width=1600, height=105)

        window_colour = 'grey90'
        self.configure(background=window_colour)

        # Frame 1
        self.__frame1 = tk.Frame(self, background=window_colour)
        self.__user_label = ttk.Label(self.__frame1, text='Username', justify='left', anchor='w',
                                      font=('Helvetica', 16), width=10, background=window_colour)
        self.__user_label.pack(side='left')

        self.__username = tk.StringVar()  # Password variable
        self.__user_field = tk.Entry(self.__frame1, textvariable=self.__username)
        self.__user_field.pack(fill=tk.X, expand=True, side=tk.RIGHT)

        self.__frame1.pack(fill=tk.X, expand=True, padx=5, pady=5)

        # Frame 2
        self.__frame2 = tk.Frame(self, background=window_colour)
        self.__pass_label = ttk.Label(self.__frame2, text='Password', justify='left', anchor='w',
                                      font=('Helvetica', 16), width=10, background=window_colour)
        self.__pass_label.pack(side='left')

        self.__password = tk.StringVar()  # Password variable
        self.__pass_field = tk.Entry(self.__frame2, textvariable=self.__password, show='*')
        self.__pass_field.pack(fill=tk.X, expand=True, side=tk.RIGHT)

        self.__frame2.pack(fill=tk.X, expand=True, padx=5)

        # Frame 3
        self.__frame3 = tk.Frame(self, background=window_colour)
        self.__button_cancel = tk.Button(self.__frame3, text='Cancel', justify='center', anchor='ne',
                                         highlightbackground=window_colour, command=self.__event_button_cancel)
        self.__button_cancel.pack(side=tk.RIGHT)

        self.__button_ok = tk.Button(self.__frame3, text='OK', justify='center', anchor='ne',
                                     highlightbackground=window_colour, command=self.__event_button_ok)
        self.__button_ok.pack(side=tk.RIGHT)
        self.__frame3.pack(fill=tk.X, expand=True, padx=5, pady=5)

        # Try to set window focus
        if 'NSRunningApplication' in dir():
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(os.getpid())
            app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

    def __event_button_ok(self):
        self.exit_code = True
        self.__close()

    def __event_button_cancel(self):
        self.__username.set('')
        self.__password.set('')
        self.exit_code = False
        self.__close()

    def __close(self):
        # Destroy the window and mark and inactive
        self.destroy()

    def set_title(self, title):
        """
        Set title of Window and label
        :param title: (str) Title of the window
        :return: (void)
        """
        self.title(title)

    def set_username(self, username):
        """
        Set the default username and move focus to password
        :param username: (str) Username
        :return: (void)
        """
        self.__username.set(username)
        self.__pass_field.focus_force()

    def get_credentials(self, title=None, username=None):
        """
        Bring up the dialog
        :param title: (str) Title of the window
        :param username: (str) The default username
        :return: (any) Value selected or entered
        """
        # Setup window
        if title:
            self.set_title(title)
        if username:
            self.set_username(username)

        self.wm_deiconify()
        self.__user_field.focus_force()
        self.wait_window()
        return self.__username.get(), self.__password.get(), self.exit_code
