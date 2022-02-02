#!/usr/bin/env python3
"""
Script:	webkit2.py
Date:	2022-01-24	

Platform: macOS/Windows/Linux

Description:

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2022, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'


from PyObjCTools import AppHelper

from popup_cocoa_webbrowser import WebApp

if __name__ == '__main__':
    app = WebApp.sharedApplication()
    app.settings(width=768, height=1152, dark_mode=True,
                 target_url='http://www.google.com',
                 title='Search Me', instruction='Search for a webpage', button='Choose this page',
                 agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1',
                 preferred_mobile=True, javascript=True)
    AppHelper.runEventLoop()
    print('Application did not exit gracefully')
