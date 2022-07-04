#!/usr/bin/python3
#Vídeo 10 da playlist https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

print("import os\n")

import os

print("print(dir(os))\nResposta:\n", dir(os))

print("\nprint(os.getcwd())\nResposta:", os.getcwd())

os.chdir('/home/alisson/Documentos/Sistemas Embarcados II/SEII-Alisson-Carvalho-Vasconcelos')

print("\nos.chdir('/home/alisson/Documentos/Sistemas Embarcados II/SEII-Alisson-Carvalho-Vasconcelos')\n\nprint(os.getcwd())\nResposta:", os.getcwd())

os.chdir('/home/alisson/Documentos/Sistemas Embarcados II/SEII-Alisson-Carvalho-Vasconcelos/Semana 04')

print("\nprint(os.listdir())\nResposta:\n",os.listdir())

os.mkdir('OS-Demo')
os.makedirs('OS-Demo-2/Sub-dir-1')

print("\nos.mkdir('OS-Demo')\nos.makedirs('OS-Demo-2/Sub-dir-1')\n\nprint(os.listdir())\n\nprint(os.listdir('OS-Demo-2'))\nResposta:\n",os.listdir())
print(os.listdir())

os.rmdir('OS-Demo')
os.removedirs('OS-Demo-2/Sub-dir-1')

print("\nos.rmdir('OS-Demo')\nos.removedirs('OS-Demo-2/Sub-dir-1')\n\nprint(os.listdir())\nResposta:\n",os.listdir())

os.mkdir('OS-Demo')
os.rename('OS-Demo', 'Teste')

print("\nos.mkdir('OS-Demo')\nos.rename('OS-Demo', 'Teste'))\n\nprint(os.listdir())\nResposta:\n",os.listdir())

os.removedirs('Teste')

print("\nos.stat('demo.txt')\nResposta:", os.stat('demo.txt'))
print("\nprint(os.stat('demo.txt).st_mtime)\nResposta:", os.stat('demo.txt').st_mtime)

from datetime import datetime as dt

mod_time = os.stat('demo.txt').st_mtime
print("\nfrom datetime import datetime\n\nmod_time = os.stat('demo.txt').st_mtime\nprint(datetime.fromtimestamp(mod_time))\nResposta:", dt.fromtimestamp(mod_time))

print("\nfor dirpath, dirnames. filenames in os.walk('/home/Documentos/Sistemas Embarcados II/SEII-Alisson-Carvalho-Vasconcelos')")
print("\tprint('Current Path:', dirpath)\n\tprint('Directories:', dirnames)\n\tprint('Files:', filenames)\nResposta:")

for dirpath, dirnames, filenames in  os.walk('/home/alisson/Documentos/Sistemas Embarcados II/SEII-Alisson-Carvalho-Vasconcelos'):
	print('Current Path:', dirpath,'\nDirectories:', dirnames,'\nFiles:', filenames)
	print()

print("print(os.environ.get('HOME'))\nResposta:", os.environ.get('HOME'))

file_path = os.environ.get('HOME') + 'test.txt'

print("\nfile_path = os.environ.get('HOME') + 'test.txt'\n\nprint(file_path)\nResposta:", file_path)

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

print("\nfile_path = os.path.join(os.environ.get('HOME'), 'test.txt')\n\nprint(file_path)\nResposta:", file_path)

print("\nos.path.basename('/tmp/test.txt')\nResposta:", os.path.basename('/tmp/test.txt'))
print("\nos.path.dirname('/tmp/test.txt')\nResposta:", os.path.dirname('/tmp/test.txt'))
print("\nos.path.split('/tmp/test.txt')\nResposta:", os.path.split('/tmp/test.txt'))
print("\nos.path.exists('/tmp/test.txt')\nResposta:", os.path.exists('/tmp/test.txt'))
print("\nos.path.isdir('/tmp/test')\nResposta:", os.path.isdir('/tmp/test'))
print("\nos.path.isfile('/tmp/test')\nResposta:", os.path.isfile('/tmp/test'))
print("\nos.path.splitext('/tmp/test.txt')\nResposta:", os.path.splitext('/tmp/test.txt'))

print("\nprint(dir(os.path))\nResposta:\n",dir(os.path))##
