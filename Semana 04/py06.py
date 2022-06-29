#!/usr/bin/python3
#Vídeo 06 da playlist https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

if True:
	print("if True:\n\tprint('Conditional was True')\nResposta: Conditional was true\n\nif False:\n\tprint('Conditional was True')\nResposta:")

if False:
	print('Conditional was True')

language = 'Python'

print("\nlanguage = 'Python'\n\nif language == 'Python':\n\tprint('Language is Python')")
print("elif language == 'Java'\n\tprint('Language is Java')\nelse:\n\tprint('No match')")

if language == 'Python':
	print('Resposta: Language is Python')
elif language == 'Java':
	print('Resposta: Language is Java')
else:
	print('Resposta: No match')

language = 'Java'

print("\nlanguage = 'Java'\n\nif language == 'Python':\n\tprint('Language is Python')")
print("elif language == 'Java'\n\tprint('Language is Java')\nelse:\n\tprint('No match')")

if language == 'Python':
	print('Resposta: Language is Python')
elif language == 'Java':
	print('Resposta: Language is Java')
else:
	print('Resposta: No match')

language = 'JavaScript'

print("\nlanguage = 'JavaScript'\n\nif language == 'Python':\n\tprint('Language is Python')")
print("elif language == 'Java'\n\tprint('Language is Java')\nelse:\n\tprint('No match')")

if language == 'Python':
	print('Resposta: Language is Python')
elif language == 'Java':
	print('Resposta: Language is Java')
else:
	print('Resposta: No match')

user = 'Admin'
logged_in = True

print("\nuser = 'Admin'\nlogged_in = True\n\nif user == 'Admin' and logged_in:\n\tprint('Admin Page')")
print("else:\n\tprint('Bad Creds')")

if user == 'Admin' and logged_in:
	print('Resposta: Admin Page')
else:
	print('Resposta: Bad Creds')

logged_in = False

print("\nlogged_in = False\n\nif user == 'Admin' and logged_in:\n\tprint('Admin Page')")
print("else:\n\tprint('Bad Creds')")

if user == 'Admin' and logged_in:
	print('Resposta: Admin Page')
else:
	print('Resposta: Bad Creds')

print("\nif user == 'Admin' or logged_in:\n\tprint('Admin Page')")
print("else:\n\tprint('Bad Creds')")

if user == 'Admin' or logged_in:
	print('Resposta: Admin Page')
else:
	print('Resposta: Bad Creds')

print("\nif not logged_in:\n\tprint('Please Log In')")
print("else:\n\tprint('Welcome')")

if not logged_in:
	print('Resposta: Please Log In')
else:
	print('Resposta: Welcome')

a = [1, 2, 3]
b = [1, 2, 3]

print("\na = [1, 2, 3]\nb = [1, 2, 3]\n\nprint(a == b)\nResposta:", a == b,"\n\nprint(a is b)\nResposta:", a is b)
print("\n\nprint(id(a))\nResposta:", id(a),"\nprint(id(b))\nResposta:", id(b))

b = a

print("\nb = a\n\nprint(id(a))\nResposta:", id(a),"\nprint(id(b))\nResposta:", id(b),"\n\nprint(a is b)\nResposta:", a is b)
