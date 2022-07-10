#!/usr/bin/python3
#Vídeo 16 da playlist https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as d_f:
	csv_d = csv.reader(d_f)

	print(csv_d,"\n")
	print(list(csv_d),"\n")

	d_f.seek(0)

	for line in csv_d:
		print(line)

	d_f.seek(0)
	next(csv_d)
	next(csv_d)
	print()

	for line in csv_d:
		print(line)

	d_f.seek(0)
	next(csv_d)
	next(csv_d)

	for line in csv_d:
		names.append(f"{line[0]} {line[1]}")

print()

for name in names:
	print(name)

names = []

with open('patrons.csv', 'r') as d_f:
	csv_d = csv.reader(d_f)

	next(csv_d)
	next(csv_d)

	for line in csv_d:
		if line[0] == 'No Reward':
			break
		names.append(f"{line[0]} {line[1]}")

print()

for name in names:
	print(name)

print()
html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in (names):
	html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)

print()
html_output = ''
names = []

with open('patrons.csv', 'r') as d_f:
	csv_d = csv.DictReader(d_f)

	for item in csv_d:
		print(item)

	d_f.seek(0)
	next(csv_d)
	next(csv_d)

	for line in csv_d:
		if line['FirstName'] == 'No Reward':
			break
		names.append(f"{line['FirstName']} {line['LastName']}")

print()

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in (names):
	html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)
