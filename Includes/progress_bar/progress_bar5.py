#!/usr/bin/env python3

"""
Script:	progress_bar5.py
Date:	2018-09-24

Platform: MacOS

Description:
Creates a GUI progress bar
Customisable colour, title and header

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2018, thedzy'
__license__ = 'GPL'
__version__ = '5.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'

import tkinter as tk
from tkinter import ttk


class ProgressBar(tk.Tk):
    """
    Class to create a visual progress bar
    """

    def __init__(self, max_size=100, title='', width=720, bar_colour='#00ff00', back_colour='#ffffff',
                 determinate=True, *args, **kwargs):
        # Initialise as a tkinter class
        tk.Tk.__init__(self, *args, **kwargs)

        # Initialise the variables
        self.label_value = None
        self.label = None
        self.progress = None

        # Initialise the draw
        self.create_window()
        self.geometry('{:d}x{:d}'.format(width, 0))

        # Set options
        self.set_title(title)
        self.set_colour(bar_colour, back_colour)
        self.set_determinate(determinate)

        # Initialise positions
        self.set_max(max_size)
        self.set_position(0)

        # Refresh the window
        self.__refresh()

        # Flag app as active, tracking a close
        self.active = True

        # Destroy the window if the app is closed
        self.protocol('WM_DELETE_WINDOW', self.close)

    def create_window(self):
        # Set min/max sizing for resizing
        self.minsize(width=200, height=50)
        self.maxsize(width=1600, height=50)

        window_color = 'grey90'
        self.configure(background=window_color)

        # Set progress bar style
        style = ttk.Style()
        style.theme_use('default')
        style.configure('black.Horizontal.TProgressbar', background='red')

        # Define Label
        self.label_value = tk.StringVar(value='Loading...')
        self.label = ttk.Label(self.master, text='', justify='left', anchor='w', textvariable=self.label_value,
                               font=('Helvetica', 16), background=window_color)
        self.label.pack(fill=tk.BOTH, expand=True, padx=5)

        # Define Progress bar
        self.progress = ttk.Progressbar(self, orient='horizontal', length=300, mode='determinate')
        self.progress.pack(fill=tk.BOTH, expand=True)

    def set_title(self, title):
        """
        Set title of Window title
        :param title: (str) Text of the window label
        :return: (void)
        """

        self.title(str(title))

        self.__refresh()

    def set_label(self, title):
        """
        Set title of Window label
        :param title: (str) Text of the window label
        :return: (void)
        """

        self.label_value.set(str(title))

        self.__refresh()

    def set_position(self, position):
        """
        Set bar position value
        :param position: (int) Position of the progress
        """

        self.progress['value'] = position

        self.__refresh()

    def get_position(self):
        """
        Get bar position value
        :return: (int) Position of the progress
        """

        return self.progress['value']

    def increment(self, increment):
        """
        Increment the bar by a value
        :param increment: (int) Value to increment by
        """

        self.progress.step(increment)

        self.__refresh()

    def set_max(self, value):
        """
        Set Bar Maximum value
        :param value: (int) The maximum value of the progress bar
        """

        self.progress['maximum'] = value

        self.__refresh()

    def get_max(self):
        """
        Set Bar Maximum value
        :return: (int) The maximum value of the progress bar
        """

        return self.progress['maximum']

    def set_colour(self, bar_colour=None, back_colour=None):
        """
        Set the bar foreground and background
        :param bar_colour: (string) hex, (string) named, (tuple)(int) 0-55 rgb, (tuple)(float) 0-1 rgb
            Examples: 'black', 'yellow', 'white', 'green', 'grey', 'red', 'blue', 'orange', 'grey45'
        :param back_colour: (string) hex, (string) named, (tuple)(int) 0-55 rgb, (tuple)(float) 0-1 rgb
            Examples: 'black', 'yellow', 'white', 'green', 'grey', 'red', 'blue', 'orange', 'grey45'
        """

        style = ttk.Style()
        style.theme_use('default')
        new_bar_colour = style.lookup('Horizontal.TProgressbar', 'background')
        new_back_colour = style.lookup('Horizontal.TProgressbar', 'troughcolor')

        if bar_colour:
            new_bar_colour = self.to_hex(bar_colour)

        if back_colour:
            new_back_colour = self.to_hex(back_colour)

        style.configure('Horizontal.TProgressbar', background=new_bar_colour, troughcolor=new_back_colour)

        self.__refresh()

    @staticmethod
    def to_hex(colour):
        if colour[0] == '#' and len(colour) == 7:
            return colour
        elif all([isinstance(rgb, int) for rgb in colour]):
            return '#{0:02x}{1:02x}{2:02x}'.format(colour[0], colour[1], colour[2])
        elif all([isinstance(rgb, float) for rgb in colour]):
            return '#{0:02x}{1:02x}{2:02x}'.format(int(colour[0] * 255), int(colour[1] * 255), int(colour[2] * 255))
        else:
            return colour

    def set_determinate(self, determinate=True):
        """
        Toggle the style from determinate to indeterminate
        :param determinate: (bool) Is determinate
        """

        if determinate:
            self.progress['mode'] = 'determinate'
            print(self.progress['mode'])
            print('wtf')
        else:
            self.progress['mode'] = 'indeterminate'
            print('no')

        self.__refresh()

    def __refresh(self):
        # Refresh window
        self.update_idletasks()
        self.update()

    def close(self):
        # Destroy the window and mark and inactive
        self.destroy()
        self.active = False

    def is_active(self):
        """
        Return whether the window is inactive to prevent errors in calling for updates
        :return: (bool) Is active
        """
        return self.active
