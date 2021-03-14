#!/usr/bin/env python3

"""
Script:	userpass.py
Date:	2010-01-27

Platform: MacOS

Description:
Creates a GUI input dialog using the PyObjC framework

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2019, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'

try:
    from AppKit import *
    import Foundation
    import Cocoa
except ImportError as err:
    print(err)
    print('You need to have the PyObjC frameworks installed')
    print('easy_install -U pyobjc')


class Alert(object):
    """
    Alert (Class)
    Create a message dialog and get user response
    """

    WARNING = NSWarningAlertStyle
    INFORMATIONAL = NSInformationalAlertStyle
    CRITICAL = NSCriticalAlertStyle

    def __init__(self, messageText, **kwargs):
        """
        __init__
        Initialise dialog
        :param messageText: 'The message for the dialog
        :param kwargs:
            informativeText = Information below the alert message (string)
            icon = Path to icon (string)
            buttons = Button texts (list, strings)
            style = WARNING, INFORMATIONAL or CRITICAL
        """
        super(Alert, self).__init__()
        self.messageText = messageText
        self.informativeText = kwargs.get('informativeText', '')
        self.icon = kwargs.get('icon', None)
        self.buttons = kwargs.get('buttons', ['OK'])
        if not kwargs.get('style', self.INFORMATIONAL) in [self.WARNING, self.INFORMATIONAL, self.CRITICAL]:
            self.style = self.INFORMATIONAL
        else:
            self.style = kwargs.get('style', self.INFORMATIONAL)

    def display(self):
        """
        Display the message and return the result
        :return: Button Index (integer)
        """
        alert = UIAlertView.alloc().initWithTitle()
        alert.setMessageText_(self.messageText)
        alert.setInformativeText_(self.informativeText)
        try:
            if self.icon is not None:
                image = NSImage.alloc().initByReferencingFile_(self.icon)
                alert.setIcon_(image)
        except:
            pass
        alert.setAlertStyle_(self.style)
        for button in reversed(self.buttons):
            alert.addButtonWithTitle_(button)
        NSApp.activateIgnoringOtherApps_(True)
        self.buttonPressed = alert.runModal()
        return len(self.buttons) - (self.buttonPressed - 1000) - 1


if __name__ == '__main__':
    alert = Alert('Hello')
    alert.display()
