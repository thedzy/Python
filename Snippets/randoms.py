#!/usr/bin/env python3

import random
import string
import os
import secrets

# DIGITS, 0-32768
print(random.randrange(0,32768))

# DIGITS, 1-10
print(random.randrange(0,10))

# Random character
print(random.choice(string.ascii_letters))

# BASE64, 48 alphanumeric characters
print(secrets.token_urlsafe(48))

# Hex, 16 characters
print("".join([random.choice('ABCDEF1234567890') for i in range(32)]))

# Hex, 16 characters
print(os.urandom(16).hex())

# Hex, 16 characters
print(secrets.token_hex(16))

# Random characters, beyond basic Latin alphabet
print(os.urandom(16).decode("utf-16"))

# BASE64, 12 alphanumeric characters
print("".join([random.choice(string.ascii_letters + string.digits) for i in range(32)]))

# DIGITS, 0-99999999 (8 digits formatted)
print("".join([str(random.randrange(0,9)) for i in range(8)]))
