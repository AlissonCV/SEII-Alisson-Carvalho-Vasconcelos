#!/usr/bin/python3
'''
Vídeo 18 da playlist https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

LEGB
Local: variáveis que são definidas dentro de uma função
Enclosing: são variáveis na capacidade local de abrangência de funções
Global: são variáveis definidas no nivel superior do módulo ou explicitamente declarada global, usando a palavra-chave
Built-in: são somente nomes que são pré-atribuídos no Python
'''

x = 'global x'

def test():
	y = 'local y'
	print(y + '\n\n' + x)

test()

'''
print(y)

Traceback (most recent call last):
  File "/home/alisson/Documentos/Sistemas Embarcados II/SEII-Alisson-Carvalho-Vasconcelos/Semana 04/./py18.py", line 20, in <module>
    print(y)
NameError: name 'y' is not defined
'''

print(x)

x1 = 'global x'

def test():
	x = 'local x'

	print('\n' + x)

test()
print(x)

def test():
	global x1
	x1 = 'local x'

	print('\n' + x1)

test()
print(x1)

def test(z):
	print('\n' + z)

test('local z')

'''
mim() é uma função do python com uma palavra chave
'''

m = min([5, 1, 3, 4, 2])

print('\n' + str(m))

import builtins

'''
#print(dir(builtins))

def min():
	pass

m = min([5, 1, 3, 4, 2])

print('\n' + str(m))

Traceback (most recent call last):
  File "/home/alisson/Documentos/Sistemas Embarcados II/SEII-Alisson-Carvalho-Vasconcelos/Semana 04/./py18.py", line 70, in <module>
    m = min([5, 1, 3, 4, 2])
TypeError: min() takes 0 positional arguments but 1 was given
'''

def my_min():
	pass

m = min([5, 1, 3, 4, 2])

print('\n' + str(m))

def outer():
	x = 'outer x'

	def inner():
		x = 'inner x'
		print('\n' + x)

	inner()
	print(x)

outer()

def outer():
	x = 'outer x'

	def inner():
		#x = 'inner x'
		print('\n' + x)

	inner()
	print(x)

outer()

def outer():
	x = 'outer x'

	def inner():
		nonlocal x
		x = 'inner x'
		print('\n' + x)

	inner()
	print(x)

outer()

def outer():
	x = 'outer x'

	def inner():
		nonlocal x
		x = 'inner x'
		print('\n' + x)

	inner()
	print(x)

outer()

print(x)

def outer():
	x = 'outer x'

	def inner():
		print('\n' + x)

	inner()
	print(x)

outer()

print(x)

def outer():
	def inner():
		print('\n' + x)

	inner()
	print(x)

outer()

print(x)
