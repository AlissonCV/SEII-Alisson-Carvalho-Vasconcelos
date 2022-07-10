#!/usr/bin/python3
#Vídeo 14 da playlist https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

import os

os.chdir('/home/alisson/Documentos/Sistemas Embarcados II/SEII-Alisson-Carvalho-Vasconcelos/Semana 04/Video/')

print(os.getcwd())

for f in os.listdir():
    print(f)

print()

for f in os.listdir():
    print(os.path.splitext(f))

print()

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    print(f_name)

print()

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    print(f_name.split('-'))

print()

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    print(f_title)

print()

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    print(f_course)

print()

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    print(f_num)

print()

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))

print()

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()
    print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))

print()

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:]
    print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))

print()

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)
    print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))

print()

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    f_title = f_title.strip()
    f_num = f_num.strip()[1:].zfill(2)
    print('{}-{}{}'.format(f_num, f_title, f_ext))

print()

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    f_title = f_title.strip()
    f_num = f_num.strip()[1:].zfill(2)
    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    os.rename(f, new_name)
