#Cálcula la potencia de una señal senoidal con periodo de 2 segundos y sin desfase
import numpy as np
t=np.arange(0,10,0.001) #Dominio 
A=1;
T=2; #Periodo
theta=0; #fase
y=np.sin((2*np.pi/T)*t+theta); #funcion senoidal
P=np.sum(np.power(y,2))/len(y) #La integral se aproxima como una suma promediada
