'''
In this lab, you'll change the username of your coworker Jane Doe from "jane" to "jdoe" in compliance with company's naming policy. The username change has already been done. However, some files that were named with Jane's previous username "jane" haven't been updated yet. To help with this, you'll write a bash script and a Python script that will take care of the necessary rename operations.

- Practice using the cat, grep, and cut commands for file operations
- Use > and >> commands to redirect I/O stream
- Replace a substring using Python
- Run bash commands in Python
'''


#!/usr/bin/env python3

import sys
import subprocess

f = open(sys.argv[1], "r")
for line in f.readlines():
  old_name = line.strip()
  new_name = old_name.replace("jane", "jdoe")
  subprocess.run(["mv", old_name, new_name])
f.close()

