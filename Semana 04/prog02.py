#!/usr/bin/python3

import urllib.request

ex1 = 'http://www.blankwebsite.com/'
ex2 = 'http://www.python.org/'

print('\nConteúdo da página:')

with urllib.request.urlopen(ex1) as f:
	print(f.read(1000).decode('utf-8')) # Primeiros 1000 bytes

print("\n")

with urllib.request.urlopen(ex2) as f:
	print(f.read(1000).decode('utf-8')) # Primeiros 1000 bytes