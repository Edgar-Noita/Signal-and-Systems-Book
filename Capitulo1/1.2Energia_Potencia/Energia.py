t=np.arange(0,1,0.001) #Dominio
y=2*t; #funcion senoidal
E=np.sum(np.power(y,2))/len(y); #La integral se aproxima como una suma promediada
