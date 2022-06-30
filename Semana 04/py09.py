#!/usr/bin/python3
#Vídeo 09 da playlist https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

print("import my_module\n")

import my_module

print("\ncourses = ['History', 'Math', 'Physics', 'CompSci']\n")

courses = ['History', 'Math', 'Physics', 'CompSci']

print("index = my_module.find_index(courses, 'Math')")

index = my_module.find_index(courses, 'Math')
print("print(index) =", index)

print("\nimport my_module as mm\n")

import my_module1 as mm

print("\ncourses = ['History', 'Math', 'Physics', 'CompSci']\n")

print("index = mm.find_index(courses, 'Math')")

index_1 = mm.find_index(courses, 'Math')
print("\nprint(index) =", index_1)

print("\nfrom my_module import find_index\n")

from my_module2 import find_index

print("\ncourses = ['History', 'Math', 'Physics', 'CompSci']\n")

print("index = find_index(courses, 'Math')")

index_2 = find_index(courses, 'Math')
print("\nprint(index) =", index_2)

print("\nfrom my_module import find_index as fi\n")

from my_module3 import find_index as fi

print("\ncourses = ['History', 'Math', 'Physics', 'CompSci']\n")

print("index = fi(courses, 'Math')")

index_3 = fi(courses, 'Math')
print("\nprint(index) =", index_3)

print("\nimport sys\n\nprint(sys.path)\n")

import sys

print(sys.path)

print("\nsys.path.append('/home/alisson/Downloads/My_Modules')")

print("\nfrom my_module import find_index\n")

from my_module4 import find_index

print("\ncourses = ['History', 'Math', 'Physics', 'CompSci']\n")

print("index = find_index(courses, 'Math')")

index_4 = find_index(courses, 'Math')
print("\nprint(index) =", index_4)

print("\nimport random")

import random as rd

print("\ncourses = ['History', 'Math', 'Physics', 'CompSci']\n")

print("random = random.choice(courses)")

aux = rd.choice(courses)
print("\nprint(random) =", aux)

print("\nimport math")

import math

print("\nrads = math.radians(90)")

aux1 = math.radians(90)
print("\nprint(rads) =", aux1,"\nprint(math.sin(rads)) =", math.sin(aux1))

print("\nimport datetime\nimport calendar\n\ntoday = datetime.date.today()")

import datetime
import calendar

today = datetime.date.today()
print("print(today) =", today,"\nprint(calendar.isleap(2017)) =", calendar.isleap(2017),"\nprint(calendar.isleap(2020))", calendar.isleap(2020))

print("\nimport os")

import os

print("\nprint(os.getcwd()) =", os.getcwd(),"\nprint(os.__file__) =", os.__file__)
