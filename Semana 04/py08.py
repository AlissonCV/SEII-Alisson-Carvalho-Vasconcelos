#!/usr/bin/python3
#Vídeo 08 da playlist https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

print("def hello_func():\n\tpass\nprint(hello_func())")

def hello_func_1():
	pass
print("Resposta:", hello_func_1(),"\n\ndef hello_func():\n\tprint('Hello Function!')\n\nhello_func()")

def hello_func_2():
	print('Resposta: Hello Function!')

hello_func_2()

print("\n\ndef hello_func():\n\treturn 'Hello Function.'\n\nhello_func()\nhello_func()\nprint(hello_func())\nprint(hello_func().upper())\nResposta:")

def hello_func_3():
	return 'Hello Function.'

hello_func_3()
hello_func_3()
print(hello_func_3())
print(hello_func_3().upper())


print("\n\ndef hello_func(greeting):\n\treturn '{} Function.'.format(greeting)\n\nprint(hello_func('Hi'))")

def hello_func_4(greeting):
	return '{} Function.'.format(greeting)

print("Resposta:", hello_func_4('Hi'))

print("\n\ndef hello_func(greeting, name = 'You'):\n\treturn '{}, {}'.format(greeting, name)\n\nprint(hello_func('Hi'))\nprint(hello_func('Hi', name = 'Corey'))")

def hello_func_5(greeting, name = 'You'):
	return '{}, {}'.format(greeting, name)

print("\nResposta:\n" + hello_func_5('Hi'))
print(hello_func_5('Hi', name = 'Corey'),"\n\ndef student_info(*args, **kwargs):\n\tprint(args)\n\tprint(kwargs)\n\nstudent_info('Math','Art',name='John', age=22)\nResposta:")

def student_info_1(*args, **kwargs):
	print(args)
	print(kwargs)

student_info_1('Math', 'Art', name='John', age=22)

print("\ndef student_info(*args, **kwargs):\n\tprint(args)\n\tprint(kwargs)\n\ncourses = ['Math', 'Art']\ninfo = {'name': 'John', 'age': 22}\n\nstudent_info(courses, info)\nResposta:")

def student_info_2(*args, **kwargs):
	print(args)
	print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info_2(courses, info)

print("\ndef student_info(*args, **kwargs):\n\tprint(args)\n\tprint(kwargs)\n\ncourses = ['Math', 'Art']\ninfo = {'name': 'John', 'age': 22}\n\nstudent_info(*courses, **info)\nResposta:")

def student_info_3(*args, **kwargs):
	print(args)
	print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info_2(*courses, **info)

print("\n\nmonth_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]\n\ndef is_leap(year):\n\nreturn year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)")

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	"""Return True for leap years, False for non-leap years."""

	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print("\ndef days_in_month(year, month):\n\tif not 1 <= month <= 12:\n\t\treturn 'Invalid Month'\n\n\tif month == 2 and is_leap(year):\n\t\treturn 29\n\n\treturn month_days[month]")

def days_in_month(year, month):
	"""Return number of days in that month in tha year."""

	if not 1 <= month <= 12:
		return 'Invalid Month'

	if month == 2 and is_leap(year):
		return 29

	return month_days[month]

print("\nprint(is_leap(2017))\nprint(is_leap(2020))\nprint(days_in_month(2017, 2))\nprint(days_in_month(2020, 2))\nResposta:")
print(is_leap(2017))
print(is_leap(2020))
print(days_in_month(2017, 2))
print(days_in_month(2020, 2))
