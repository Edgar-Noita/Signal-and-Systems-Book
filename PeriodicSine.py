#Implemente el siguiente código en Python para graficar una señal con una amplitud de 10, un periodo de 2, y un ángulo de desfase de 45 grados

import numpy as np

from matplotlib import pyplot as plt

t=np.arange(0,10,0.001) #Dominio 

A=10;

T=2; #Periodo

theta=np.pi/4; #fase

y=np.sin((2*np.pi/T)*t+theta); #funcion senoidal

plt.plot(t,y)
plt.grid('on') 
plt.title('Funcion senoidal con amplitude '+str(A) +'Periodo '+str(T) +' y desfase '+str(theta))
