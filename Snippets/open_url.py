#!/usr/bin/env python3

import webbrowser

print("Open in defualt browser")
webbrowser.open_new("https://google.com")

print("Open in Safari")
webbrowser.get('safari').open_new("https://google.com")
