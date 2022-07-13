#!/usr/bin/python3
#Vídeo https://www.youtube.com/watch?v=DcfYgePyedM

import numpy as np

a1 = np.array([3,5,7,3]) #cria um array de números

print('a1 =', a1)

print()
a2 = np.zeros(10) #cria um array de 10 elementos iguais a zero

print('a2 =', a2)

print()
a3 = np.ones(10) #cria um array de 10 elementos iguais a um

print('a3 =',a3)

print()
a4 = np.random.random(10) #array de números randômicos uniformemente variando de 0 a 1

print('a4 =', a4)

print()
a5 = np.random.randn(10) #array de números gaussianos normais distribuidos com uma variação em torno de zero

print('a5 =', a5)

print()
a6 = np.linspace(0, 10, 100) #array de números variando de 0 a 10 espaçados igualmente

print('a6:\n', a6)

print()
a7 = np.arange(0, 10, 0.02) #array de números variando de 0 a 10 espaçados de 0.02

print('a7:\n', a7)
