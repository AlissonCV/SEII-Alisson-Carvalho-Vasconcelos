#!/usr/bin/python3
#Vídeo 02 da playlist https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

message = 'Hello World'
message1 = 'Alisson\'s World'
message2 = "Alisson's World"
message3 = """Alisson's World was a good
cartoon in the 1990s"""
message4 = message.replace('World', 'Universe')
greeting = 'Hello'
name = 'Alisson'
message5 = greeting + ', ' + name
message6 = greeting + ', ' + name + '. Welcome!'
message7 = '{}, {}. Welcome!'.format(greeting, name)
message8 = f'{greeting}, {name}. Welcome!'
message9 = f'{greeting}, {name.upper()}. Welcome!'

print("message =",message)
print("message = 'Alisson\'s World' =",message1)
print("message = ""Alisson's World"" =",message2)
print("message = ",message3)
print("len(message) =",len(message))
print("message[0] =",message[0])
print("message[0:5] =",message[0:5])
print("message[:5] =",message[:5])
print("message[6:] =",message[6:])
print("message.lower() =",message.lower())
print("message.upper() =",message.upper())
print("message.count('Hello') =",message.count('Hello'))
print("message.count('l') =",message.count('l'))
print("message.find('World') =",message.find('World'))
print("message.find('Universe') =",message.find('Universe'))
print("message = message.replace('World', 'Universe') =",message4)
print("greeting =",greeting)
print("name =",name)
print("message = greeting + ', ' + name =",message5)
print("message = greeting + ', ' + name + '. Welcome!' =",message6)
print("message = '{}, {}. Welcome!'.format(greeting,name) =",message7)
print("message = f'{greeting}, {name}. Welcome!' =",message8)
print("message = f'{greeting}, {name.upper()}. Welcome!' =",message9)

#print(dir(name)) || print(help(str)) => imprime as funções que podem ser usadas em uma string