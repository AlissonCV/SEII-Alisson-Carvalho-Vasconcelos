#!/usr/bin/python3

import subprocess

echo_data = subprocess.call("echo 'Hello World'", shell=True)
print("\n")

#print(echo_data)

subprocess.call(["ls","/usr/", "-la"])