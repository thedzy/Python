#!/usr/bin/env python3

"""
Script:	progress_bar6.py
Date:	2018-12-09

Platform: MacOS, Windows

Description:
Creates a GUI progress bar
Customisable colour, title and header
Shows percentage and estimated time,
Can add output in the progressbar
"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2018, thedzy'
__license__ = 'GPL'
__version__ = '6.1'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
___status__ = 'Development'

import time
import tkinter as tk
from tkinter import ttk, font


class ProgressBar(tk.Tk):
    """
    Class to create a visual progress bar
    Added estimated time
    """

    def __init__(self, title='', set_max=100, foreground='#000000', background='#ffffff', height=60, determinant=True,
                 *args, **kwargs):
        # Initialise as a tkinter class
        tk.Tk.__init__(self, *args, **kwargs)

        # Set progress bar style
        self.__bar_colour = foreground
        self.__back_colour = background

        # Set starting height
        self.__window_height = height

        # Set output window
        self.__text = ''

        self.__time_start = time.time()

        # Initialise the draw
        self.__create_window()

        # Refresh the window
        self.__refresh()

        # Flag app as active, tracking a close
        self.__active = True

        # Destroy the window is the app is closed
        self.protocol('WM_DELETE_WINDOW', self.close)

        # Initialise settings
        self.set_title(title)
        self.set_max(set_max)
        self.set_determinante(determinant)
        self.set_colour(foreground, background)

    def __create_window(self):
        """
        Create window and widgets
        """

        # Set min/max sizing for resizing
        self.minsize(width=1000, height=self.__window_height)
        self.maxsize(width=self.winfo_screenwidth(), height=self.__window_height)

        window_colour = 'grey90'
        self.configure(background=window_colour)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('black.Horizontal.TProgressbar', background='red')
        style.layout('LabeledProgressbar',
                     [('LabeledProgressbar.trough',
                       {'children': [('LabeledProgressbar.pbar',
                                      {'side': 'left', 'sticky': 'ns'}),
                                     ('LabeledProgressbar.label', {'sticky': ''})],
                        'sticky': 'nswe'})])
        style.configure('LabeledProgressbar', text='00%', background='green', font=('Helvetica', 16),
                        foregroundforeground='black')

        # Define Label
        self.__labelValue = tk.StringVar(value='Loading...')
        self.__label = ttk.Label(self.master, text='', justify='left', anchor='w',
                                 textvariable=self.__labelValue, font=('Helvetica', 16), background=window_colour)
        self.__label.pack(fill=tk.X, expand=False, padx=5)

        # Define Progress bar
        self.__progress = ttk.Progressbar(self, orient='horizontal', length=300, mode='determinate',
                                          style='LabeledProgressbar')
        self.__progress.pack(fill=tk.X, expand=False)

        # Define label
        self.__status_value = tk.StringVar(value='0.0 seconds')
        self.__status = ttk.Label(self.master, text='0.0 seconds', justify='left', anchor='e',
                                  textvariable=self.__status_value, font=('Helvetica', 13), background=window_colour)
        self.__status.pack(fill=tk.X, expand=False, padx=5, pady=1)

        # Define Output
        self.__output = tk.Text(self.master, font=('Courier', 12), foreground='white', background='black')
        self.__output.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Initialise positions
        self.set_max(100)
        self.set_position(0)

    def set_title(self, title):
        """
        Set title of Window
        :param title: (string) title
        """

        self.title(title)

        self.__refresh()

    def set_label(self, label):
        """
        Set title of label
        :param label: (string) Label title
        """

        self.__labelValue.set(label)

        self.__refresh()

    def set_position(self, position):
        """
        Set Bar position value
        :param position: (int) Position
        """

        self.__progress['value'] = position

        self.__refresh()

    def get_position(self):
        """
        Get Position
        :return: (int) Position
        """

        return self.__progress['value']

    def set_increment(self, increment=1):
        """
        Increment the bar by a value
        :param increment: (int) Increment value
        """

        if self.__progress['value'] + increment < self.__progress['maximum']:
            self.__progress.step(increment)
        else:
            self.__progress['value'] = int(self.__progress['maximum'])

        self.__refresh()

    def set_max(self, max_value):
        """
        Set Bar Maximum value
        :param max_value: (int) Maximum value
        """

        # Keep the progress for hitting a true 100% and resetting
        self.__progress['maximum'] = max_value + 0.0000001

        self.__refresh()

    def get_max(self):
        """
        Get Bar Maximum value
        :return: (int) Maximum value
        """

        return self.__progress['maximum']

    def add_output(self, text, reset=False):
        """
        Add output to the progress bar, creating a text output panel
        :param text: (str) Text to add to the window
        :param reset: (bool) Clear the existing tex
        :return: (void)
        """

        if reset:
            self.__text = str(text)
        else:
            self.__text += str(text)

        self.__output.delete('1.0', tk.END)
        self.__output.insert(tk.END, self.__text + '\n')

        # Get the font size in pixels
        font_height = tk.font.Font(font=('Courier', 12)).metrics('linespace')
        self.__window_height = int(len(self.__output.get(1.0, tk.END).splitlines()) * font_height) + 70

        self.minsize(width=1000, height=self.__window_height)
        self.maxsize(width=1600, height=self.__window_height)

        self.__refresh()

    def get_output(self):
        """
        Get output to the progress bar
        :return: (str) Text of the output window
        """

        return self.__text

    def set_colour(self, bar_colour=None, back_colour=None):
        """
        Set the bar foreground and background
        :param bar_colour: (str) hex starting with #, (tuple)(int) 0-255 RGB, (tuple)(float) 0-1 RGB
        :param back_colour: hex starting with #
        """

        if bar_colour is not None:
            if bar_colour[0] == '#' and len(bar_colour) == 7:
                self.__bar_colour = bar_colour
            elif all([isinstance(colour, int) for colour in bar_colour]):
                self.__bar_colour = '#{0:02x}{1:02x}{2:02x}'.format(bar_colour[0], bar_colour[1], bar_colour[2])
            elif all([isinstance(colour, float) for colour in bar_colour]):
                self.__bar_colour = '#{0:02x}{1:02x}{2:02x}'.format(
                    int(bar_colour[0] * 255), int(bar_colour[1] * 255), int(bar_colour[2] * 255))
            else:
                print('Invalid colour for bar: %s' % bar_colour)
                self.__bar_colour = '#000000'

        if back_colour is not None:
            if back_colour[0] == '#' and len(back_colour) == 7:
                self.__back_colour = back_colour
            elif all([isinstance(colour, int) for colour in back_colour]):
                self.__back_colour = '#{0:02x}{1:02x}{2:02x}'.format(back_colour[0], back_colour[1], back_colour[2])
            elif all([isinstance(colour, float) for colour in back_colour]):
                self.__back_colour = '#{0:02x}{1:02x}{2:02x}'.format(
                    int(back_colour[0] * 255), int(back_colour[1] * 255), int(back_colour[2] * 255))
            else:
                print('Invalid colour for back: %s' % back_colour)
                self.__bar_colour = '#ffffff'

        style = ttk.Style()
        style.configure('LabeledProgressbar', background=self.__bar_colour, troughcolor=self.__back_colour)

        self.__refresh()

    # Alias color to colour
    set_color = set_colour

    def set_determinante(self, determinante=True):
        """
        Toggle the style from determinate to indeterminate
        In indeterminate, will move end to end as incrementing
        :param determinante: (bool) True (determinate)
        """

        if determinante:
            self.__progress['mode'] = 'determinate'
            self.__progress.stop()
        else:
            self.__progress['mode'] = 'indeterminate'
            self.__progress.start()

        self.__refresh()

    def __refresh(self):
        """
        Refresh the window
        """

        # Get font colour for overlay text
        style = ttk.Style()

        if str(self.__progress['mode']) == 'indeterminate':
            style.configure('LabeledProgressbar', text='')
            self.__status_value.set('')
        else:
            # Calculate time remaining
            time_lapsed = (time.time() - self.__time_start)
            try:
                time_predicted = (time_lapsed / self.__progress['value']) * (
                        self.__progress['maximum'] - self.__progress['value'])
            except ZeroDivisionError:
                time_predicted = 0

            minutes, seconds = divmod(time_predicted, 60)
            hours, minutes = divmod(minutes, 60)
            self.__status_value.set('Estimated Time Remaining: {:02.0f}:{:02.0f}:{:04.1f}'.format(
                hours, minutes, seconds))

            # Calculate percent and display
            style.configure('LabeledProgressbar',
                            text='{:02.0f}%'.format(self.__progress['value'] / self.__progress['maximum'] * 100))

        if (self.__progress['value'] / self.__progress['maximum']) > 0.5:
            if self.__colour_contrast(self.__bar_colour) < 128:
                text_colour = '#ffffff'
            else:
                text_colour = '#000000'
        else:
            if self.__colour_contrast(self.__back_colour) < 128:
                text_colour = '#ffffff'
            else:
                text_colour = '#000000'

        style.configure('LabeledProgressbar', background=self.__bar_colour, troughcolor=self.__back_colour,
                        foreground=text_colour)

        # Refresh window
        self.update_idletasks()
        self.update()

    def __colour_contrast(self, value):
        """
        0 - 254 value of perceived colour values
        """

        if value[0] == '#' and len(value) == 7:
            return self.__colour_contrast_hex(value)
        elif all([isinstance(colour, int) for colour in value]):
            return self.__colour_contrast_rgb(value[0], value[1], value[2])
        elif all([isinstance(colour, float) for colour in value]):
            return self.__colour_contrast_rgb(
                int(value[0] * 255), int(value[1] * 255), int(value[2] * 255))
        else:
            return 0

    @staticmethod
    def __colour_contrast_hex(hex_value):
        """
        0 - 254 value of perceived colour values
        """

        hex_value = hex_value.lstrip('#')
        red, green, blue = tuple(int(hex_value[i:i + 2], 16) for i in (0, 2, 4))
        colour_value = ((red * 299) + (green * 587) + (blue * 114)) / 1000
        return colour_value

    @staticmethod
    def __colour_contrast_rgb(red, green, blue):
        """
        0 - 254 value of perceived colour values
        From https://www.w3.org/TR/AERT/#color-contrast
        """

        colour_value = ((red * 299) + (green * 587) + (blue * 114)) / 1000
        return colour_value

    def close(self):
        """
        Destroy the window and mark and inactive
        :return: (void)
        """

        self.destroy()
        self.__active = False

    def is_active(self):
        """
        Return whether the window is inactive to prevent errors in calling for updates
        :return: (bool)
        """

        return self.__active
