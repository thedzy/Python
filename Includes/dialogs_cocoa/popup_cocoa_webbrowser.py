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

import objc
import WebKit
from AppKit import *
from PyObjCTools import AppHelper
import time


class WebApp(NSApplication):
    def settings(self, dark_mode: bool = None,
                 width: int = 1280, height: int = 768.0, min_width: int = 400, min_height: int = 240,
                 instruction: str = None, button: str = None, title: str = None, target_url: str = None,
                 agent: str = None, javascript: bool = True, limit_domains: list = [],
                 preferred_mobile: bool = False) -> None:
        """
        Set preferences for the window/browser creation
        :param dark_mode: Use Dark mode
        :param width: Window Width
        :param height: Window Height
        :param min_width: The smallest width the window can resize to
        :param min_height: The smallest height the window can resize to
        :param instruction: The message for the user at the bottom of the Window
        :param button: The text on the button
        :param title: The title of the window
        :param target_url: The url the browser opens to
        :param agent: The agent string of the broswer
        :param javascript: Whether Javascript is enabled
        :param limit_domains: (Not functional) List of website the browser is limited to
        :param preferred_mobile: Whether the browser should request a mobile version
        :return: None
        """
        if dark_mode:
            self.dark_mode = NSAppearanceNameDarkAqua if dark_mode else NSAppearanceNameAqua
        else:
            # Always detects as 'NSAppearanceNameAqua'?
            self.dark_mode = NSAppearance.currentAppearance().name()

        # Window size
        self.window_width, self.window_height = width, height
        self.min_width, self.min_height = min_width, min_height

        # Window content settings
        self.label_text = instruction if instruction else 'Approve the access and click "Accept"'
        self.button_title = button if button else 'Accept'
        self.window_title = title if title else 'Approve the OAuth'
        self.target_url = target_url if target_url else 'https://thedzy.com'

        # Web Configuration
        self.agent = agent
        self.javascript = javascript
        self.limit_domains = limit_domains  # Not working

        # Desktop/Mobile
        self.content_mode = WebKit.WKContentModeMobile if preferred_mobile else WebKit.WKContentModeDesktop

        return

    def finishLaunching(self):
        """
        PYobjc class function
        When app launches
        :return:
        """
        NSLog('Building Window')

        # Set info.plist vales
        plist = dict(
            WKAppBoundDomains=self.limit_domains
        )
        self.setValuesForKeysWithDictionary_(plist)

        if len(self.limit_domains) > 0:
            print(f'Limit browsing to {self.valueForKey_("WKAppBoundDomains")}')

        # Set dark/light mode
        app_appearance = NSAppearance.appearanceNamed_(self.dark_mode)
        self.setAppearance_(app_appearance)

        # Get screen size
        screen_frame = NSScreen.mainScreen().frame()

        # Centre window
        window_x_coord = (screen_frame.size.width - self.window_width) / 2
        window_y_coord = (screen_frame.size.height - self.window_height) / 2

        # Create window
        window_frame = ((window_x_coord, window_y_coord), (self.window_width, self.window_height))
        window_mask = NSTitledWindowMask | NSResizableWindowMask
        self.window = NSWindow.alloc()
        self.window.initWithContentRect_styleMask_backing_defer_(window_frame, window_mask,
                                                                 NSBackingStoreBuffered, False)
        self.window.setTitle_(self.window_title)
        self.window.setContentMinSize_(NSSize(self.min_width, self.min_height))
        self.window.setLevel_(NSFloatingWindowLevel)
        self.window.setReleasedWhenClosed_(True)

        # Configure WebView
        web_config = WKWebViewConfiguration.alloc().init()
        web_prefs = WKWebpagePreferences.alloc().init()
        web_prefs.setPreferredContentMode_(self.content_mode)
        web_prefs.setAllowsContentJavaScript_(self.javascript)
        self.web_store = WebKit.WKWebsiteDataStore.alloc().init()
        web_config.setDefaultWebpagePreferences_(web_prefs)
        web_config.setWebsiteDataStore_(self.web_store)
        web_config.setApplicationNameForUserAgent_(self.agent)
        web_config.setLimitsNavigationsToAppBoundDomains_(True if len(self.limit_domains) > 0 else False)
        web_url = NSURL.alloc().initWithString_(self.target_url)
        self.addObject_toPropertyWithKey_(web_url.host(), 'WKAppBoundDomains')

        # Create WebView
        self.webkit = WKWebView.alloc().initWithFrame_configuration_(
            ((0, 50), (self.window_width, self.window_height - 50)),
            web_config)
        self.webkit.setAutoresizingMask_(NSViewMinXMargin | NSViewMaxYMargin | NSViewWidthSizable | NSViewHeightSizable)
        self.webkit.setContentStyle_(self.content_mode)
        self.webkit.setCustomUserAgent_(self.agent)
        self.webkit.setAllowsBackForwardNavigationGestures_(True)
        self.webkit.loadRequest_(NSURLRequest.alloc().initWithURL_(web_url))

        # Create button
        button_frame = ((10.0, 10.0), (80.0, 30.0))
        self.button = NSButton.alloc().initWithFrame_(button_frame)
        self.button.setTitle_(self.button_title)
        self.button.sizeToFit()
        new_size = self.button.frame().size
        self.button.setFrame_(((self.window_width - new_size.width - 40, 10), (new_size.width + 20, 30)))
        self.button.setAutoresizingMask_(NSViewMinXMargin)
        self.button.setBezelStyle_(NSBezelStyleRegularSquare)
        self.button.setAction_('submit:')
        self.button.setEnabled_(True)

        # Create label
        label_font = NSFont.systemFontOfSize_(15)
        label_width, label_height = self.window_width, 25.0
        label_frame = ((10, 10.0), (label_width, label_height))
        self.label = NSTextField.alloc().initWithFrame_(label_frame)
        self.label.setStringValue_(self.label_text)
        self.label.setAutoresizingMask_(NSViewMaxXMargin | NSViewWidthSizable)
        self.label.setFont_(label_font)
        self.label.setAlignment_(NSLeftTextAlignment)
        self.label.setDrawsBackground_(False)
        self.label.setBordered_(False)
        self.label.setEditable_(False)
        self.label.setSelectable_(False)

        # Add elements
        self.window.contentView().addSubview_(self.webkit)
        self.window.contentView().addSubview_(self.label)
        self.window.contentView().addSubview_(self.button)

        # Display
        self.window.display()
        self.window.orderFrontRegardless()

    @staticmethod
    def method(obj, exclude=r'^$', include=r'_.*'):
        import re
        methods = [item for item in dir(obj) if
                   re.search(include, item, re.IGNORECASE) and not re.search(exclude, item, re.IGNORECASE)]
        print('\n'.join(methods))

        return methods

    def submit_(self, sender):
        NSLog('Closing Window')

        sender.setEnabled_(False)
        self.window._close()

        javascript = 'document.documentElement.outerHTML.toString()'  # Get all html
        javascript = 'document.title.toString()'  # Get title

        self.webkit.evaluateJavaScript_completionHandler_(javascript, self.get_html)

    @staticmethod
    def get_html(value, error=None):
        NSLog('Getting html')
        NSLog(f'Title Element is "{value}"')
        for _ in range(10):
            print('Todo: Insert code')
            time.sleep(.1)
        NSLog(AppHelper.stopEventLoop())
        return
