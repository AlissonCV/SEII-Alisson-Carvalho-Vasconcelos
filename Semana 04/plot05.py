#!/usr/bin/python3
#Vídeo https://www.youtube.com/watch?v=1-R5b3dTvhs

import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(0,1000,1) #cria a variável x1 de 1 a 1000 incrementando os valor>

plt.plot(x1,x1**2) #cria a relação entre x1 e x1 elevado ao quadrado
plt.show() #mostra a figura que está sendo trabalhada
