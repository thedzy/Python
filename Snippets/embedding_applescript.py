#!/usr/bin/env python3

import os

import objc
from Foundation import NSAppleScript

objc.loadBundle('OSAKit', bundle_path='/System/Library/Frameworks/OSAKit.framework', module_globals=globals())

source = """
Tell application "System Events"
    with timeout of 900 seconds
        display dialog "Please enter your company username:" default answer "" with icon file ":System:Library:CoreServices:CoreTypes.bundle:Contents:Resources:UserIcon.icns" with title "Login Password" with text buttons {"Ok"} default button 1 giving up after 700
    end timeout
end tell
text returned of result
"""
sourcefile = "/tmp/" + os.path.basename(__file__) + os.urandom(16).hex() + ".applescript"
with open(sourcefile, "w+") as file:
    file.write(source)

"""
Running a AppleScript Embedded
"""
script = NSAppleScript.alloc().initWithSource_(source)

# Compile and run
if script.compileAndReturnError_(None)[0]:
    result, err = script.executeAndReturnError_(None)
    if not err:
        print("Result from embedded:")
        print(result.stringValue())
else:
    print("Failed Compile")

"""
Running a AppleScript File
"""
script, err = NSAppleScript.alloc().initWithContentsOfURL_error_(NSURL.fileURLWithPath_(sourcefile), None)

# Compile and run
if not err:
    if script.compileAndReturnError_(None):
        result, err = script.executeAndReturnError_(None)
        if not err:
            print("Result from file:")
            print(result.stringValue())
    else:
        print("Failed Compile")
else:
    print("Error loading file")

