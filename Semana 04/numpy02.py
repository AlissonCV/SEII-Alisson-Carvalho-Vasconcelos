#!/usr/bin/python3
#Vídeo https://www.youtube.com/watch?v=DcfYgePyedM

import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([3,5,7,3]) #cria um array de números
a4 = np.random.random(10) #array de números randômicos uniformemente variando de 0 a 1

'''
operações com array:
  2*a1 #multiplicação
  1/a1 #divisão dos elementos
  a1>4 #comparação dos elementos
  a1%4 #resto da divisão dos elementos por 4
  1/a1 + 2 #divisão e soma dos elementos

a1[a1>4] #seleciona os elementos que satisfazem a condição >4
'''

print('2*a1:', 2*a1)

print()
print('1/a1:', 1/a1)

print()
print('a1>4:', a1>4)

print()
print('a1[a1>4]:', a1[a1>4])

print()
print('1/a1 + 2:', 1/a1 + 2)

print()
print('1/a1 + a1 + 2:', 1/a1 + a1 + 2)

print()
x = np.linspace(0, 1, 100) #array de números variando de 0 a 1 espaçados igualmente

print('x:')
print(x, '\n\nx**2:')

print(x**2,'\n')

y = x**2 #obtem o quadrado dos elementos

plt.plot(x, y) #plota um gráfico de x por y
plt.show() #mostra o gráfico

plt.hist(a4) #plota um gráfico no formato de instagramas
plt.show() #mostra o gráfico

def f(x): #define uma funão para retornar o cálculo de uma equação
    return x**2 * np.sin(x) / np.exp(-x) #retorna o resultado da equação

x = np.linspace(0,10,100) #array de números variando de 0 a 10 espaçados igualmente
y = f(x) #obtem o cálculo da equação para cada elemento de x

plt.plot(x,y) #plota o gráfico dos elementos
plt.show() #mostra o gráfico
