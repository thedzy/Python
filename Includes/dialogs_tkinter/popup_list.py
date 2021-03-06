#!/usr/bin/env python3

"""
Script:	popup_list.py
Date:	2018-09-30

Platform: MacOS/Windows

Description:
Creates a GUI list selection with only 1 selection

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


class PopupList(tk.Tk):
    """
    Class to create a list dialog
    """

    def __init__(self, title='List', question='Please select:', list_items=(), *args, **kwargs):
        # Initialise as a tkinter class
        tk.Tk.__init__(self, *args, **kwargs)

        # Initialise the draw
        self.__create_window()

        # Default exit code
        self.exit_code = False
        self.__list_items = list_items

        # Setup window
        self.set_title(title)
        self.set_question(question)

        # Button Handlers
        self.protocol('WM_DELETE_WINDOW', self.__close)
        self.bind('<Return>', lambda event: self.__event_button_ok())

    def __create_window(self):

        # Upper center window
        x = (self.winfo_screenwidth() / 2) - 200
        y = (self.winfo_screenheight() / 3) - 45
        self.geometry('+%d+%d' % (x, y))

        # Set min/max sizing for resizing
        self.minsize(width=400, height=300)
        self.maxsize(width=2400, height=2000)

        window_colour = 'grey90'
        self.configure(background=window_colour)

        # Frame 1
        self.__frame1 = tk.Frame(self, background=window_colour)
        self.__input_label_value = tk.StringVar(value='Input:')
        self.__input_label = ttk.Label(self.__frame1, textvariable=self.__input_label_value, justify='left', anchor='w',
                                       font=('Helvetica', 16), width=10, background=window_colour)
        self.__input_label.pack(fill=tk.X, expand=True)

        self.__frame1.pack(fill=tk.X, padx=5, pady=5)

        # Frame 2
        self.__frame2 = tk.Frame(self, background=window_colour)
        self.__input = tk.StringVar()
        self.__input_field = tk.Listbox(self.master, font=('Helvetica', 16), background='white')
        self.__input_field.pack(fill=tk.BOTH, expand=True)

        self.__frame2.pack(fill=tk.BOTH, padx=5)

        # Frame 3
        self.__frame3 = tk.Frame(self, background=window_colour)
        self.__button_cancel = tk.Button(self.__frame3, text='Cancel', justify='center', anchor='ne',
                                         highlightbackground=window_colour, command=self.__event_button_cancel)
        self.__button_cancel.pack(side=tk.RIGHT)

        self.__button_ok = tk.Button(self.__frame3, text='OK', justify='center', anchor='ne',
                                     highlightbackground=window_colour,
                                     command=self.__event_button_ok)
        self.__button_ok.pack(side=tk.RIGHT)
        self.__frame3.pack(fill=tk.X, padx=5)

        # Try to set window focus
        if 'NSRunningApplication' in dir():
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(os.getpid())
            app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

    def __event_button_ok(self):
        self.exit_code = True
        self.__input = self.__input_field.get(tk.ACTIVE)
        self.__close()

    def __event_button_cancel(self):
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

    def set_question(self, question):
        """
        Set question in the label
        :param question: (str) Question in the window
        :return: (void)
        """
        self.__input_label_value.set(question)

    def set_list_items(self, list_items):
        """
        Set items for the list
        :param list_items: (list) Items to display
        :return: (void)
        """
        self.__list_items = list_items

    def get_input(self, title=None, question=None, list_items=None):
        """
        Bring up the dialog
        :param title: (str) Title of the window
        :param question: (str) Question in the window
        :param list_items: (list) Items to display
        :return: (any) Value selected or entered
        """

        # Setup window
        if title:
            self.set_title(title)
        if question:
            self.set_question(question)
        if list_items:
            self.set_list_items(list_items)
        for list_item in self.__list_items:
            self.__input_field.insert(tk.END, list_item)

        self.wm_deiconify()
        self.__input_field.focus_force()
        self.wait_window()
        return self.__input, self.exit_code
