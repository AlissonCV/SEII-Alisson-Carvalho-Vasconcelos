#!/usr/bin/python3
#Vídeo 15 da playlist https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

import csv

with open('names.csv', 'r') as csv_f:
	csv_r = csv.reader(csv_f)

	print(csv_r,"\n")

	for line in csv_r:
		print(line)

	csv_f.seek(0)
	print()

	for line in csv_r:
		print(line[2])

	csv_f.seek(0)
	print()
	next(csv_r)

	for line in csv_r:
		print(line[2])

	csv_f.seek(0)

	with open('new_names.csv', 'w') as new_f:
		csv_w = csv.writer(new_f, delimiter='-')

		for line in csv_r:
			csv_w.writerow(line)

	csv_f.seek(0)

	with open('new_namest.csv', 'w') as new_f:
		csv_w = csv.writer(new_f, delimiter='\t')

		for line in csv_r:
			csv_w.writerow(line)

print()

with open('new_namest.csv', 'r') as csv_f:
	csv_r = csv.reader(csv_f)

	for line in csv_r:
		print(line)

	csv_f.seek(0)
	csv_r = csv.reader(csv_f, delimiter='\t')
	print()

	for line in csv_r:
		print(line)

print()

with open('names.csv', 'r') as csv_f:
	csv_r = csv.DictReader(csv_f)

	for line in csv_r:
		print(line)

	csv_f.seek(0)
	print()

	for line in csv_r:
		print(line['email'])

	csv_f.seek(0)

	with open('new_namesd.csv', 'w') as new_f:
		f_names= ['first_name', 'last_name', 'email']
		csv_w = csv.DictWriter(new_f, fieldnames=f_names, delimiter='\t')

		csv_w.writeheader()
		next(csv_r)

		for line in csv_r:
			csv_w.writerow(line)

	csv_f.seek(0)

	with open('new_namesdfl.csv', 'w') as new_f:
		f_names= ['first_name', 'last_name']
		csv_w = csv.DictWriter(new_f, fieldnames=f_names, delimiter='\t')

		csv_w.writeheader()
		next(csv_r)

		for line in csv_r:
			del line['email']
			csv_w.writerow(line)
