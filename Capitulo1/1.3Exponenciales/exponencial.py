t=np.arange(0,5,0.001); #Dominio
#misma base, diferente exponente
a=2;
b1=1/3;
b2=1/2;
b3=2;
b4=3;
y1=a**(b1*t); 
y2=a**(b2*t);
y3=a**(b3*t);
y4=a**(b4*t); 
plt.subplot(2,2,1),plt.plot(t,y1), plt.title('Exponente=' +str(b1))
plt.subplot(2,2,2),plt.plot(t,y2), plt.title('Exponente=' +str(b2))
plt.subplot(2,2,3),plt.plot(t,y3), plt.title('Exponente=' +str(b3))
plt.subplot(2,2,4),plt.plot(t,y4), plt.title('Exponente=' +str(b4))
