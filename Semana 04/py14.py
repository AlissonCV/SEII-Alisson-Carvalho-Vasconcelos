#!/usr/bin/python3
#Vídeo 14 da playlist https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

import os

os.chdir('/home/alisson/Documentos/Sistemas Embarcados II/SEII-Alisson-Carvalho-Vasconcelos/Semana 04/Video/')

print(os.getcwd())

print(dir(os))

for f in os.listdir():
    print(f)
    print(os.path.splitext(f))
    f_name, f_ext = os.path.splitext(f)
    print(f_name)
    print(f_ext)
    print(file_name.split('-'))
    f_title, f_course, f_num = file_name.split('-')
    print(f_title)
    print(f_couse)
    print(f_num)
    f_title = f_title.strip()
    f_couse = f_couse.strip()
    f_num = f_num.strip()[1:].zfill(2)
    print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))
    print('{}-{}{}'.format(f_num, f_title, f_ext))
    new_name = '{}-{}{}'.format(f_num, f_title, f_ext))
    os.rename(f, new_name)
