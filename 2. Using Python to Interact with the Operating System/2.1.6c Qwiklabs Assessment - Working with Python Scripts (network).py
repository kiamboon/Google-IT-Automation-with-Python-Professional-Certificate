'''
In this lab, you'll first have to fix an incorrect Python script.

- Fixing the file permissions to make it executable.
- Fixing a bug in the code
'''


#!/usr/bin/env python3

import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

def check_connectivity():
    request = requests.get("http://www.google.com")
    return 200