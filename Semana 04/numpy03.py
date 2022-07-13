#!/usr/bin/python3
#Vídeo https://www.youtube.com/watch?v=DcfYgePyedM

import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([2,4,6,8,10]) #cria um array de números

print('\na[2]:',a1[2]) #mostra o terceiro elemento

print('\na1[2:]:',a1[2:]) #mostra do terceiro elemento ao último

print('\na1[:-2]:', a1[:-2]) #mostra os elementos excluindo os 2 últimos

print('\na1[1:-2]:', a1[1:-2]) #mostra os elementos inicando no segundo e excluindo os 2 últimos

print('\na1[::2]:', a1[::2]) #mostra os elementos iniciando do primeiro e espaçado de 2

print('\na1>3:', a1>3) #comparação dos elementos

print('\na1[a1>3]:', a1[a1>3]) #seleciona os elementos que satisfazem a condição >3

names = np.array(['Jim', 'Luke', 'Josh', 'Pete']) #cria um array de strings

print('\nnames:', names)

'''
class numpy.vectorize(pyfunc (python function or method), otypes=None, doc=None, excluded=None, cache=False,
signature=None) -> Define uma função vetorizada que recebe uma sequência aninhada de objetos ou matrizes numpy
como entradas e retorna uma única matriz numpy ou uma tupla de matrizes numpy. A função vetorizada avalia pyfunc
sobre tuplas sucessivas das matrizes de entrada, como a função python map, exceto se usar as regras de transmissão de numpy.
'''

first_letter_j = np.vectorize(lambda s: s[0])(names)=='J' # a função lambda pega o primeiro caracter da string "s", a função
							  #np.vectorize faz um loop de todos os elementos do array names,  e
							  #compara se são iguais a 'J'

print('\nfirst_letter_j:', first_letter_j)
print('\nnames[first_letter]:', names[first_letter_j]) #cria um array com as strings da variável names que começa com "J"

print('\na1%4:', a1%4)
print('\na1%4==0:', a1%4==0) #cria um array boleano indicando se os elementos de a1 são ou não divisíveis por 4
print('\na1[a1%4==0]:', a1[a1%4==0]) #cria um array de valores que são divisíveis por 4 e possui o resto igual a zero
