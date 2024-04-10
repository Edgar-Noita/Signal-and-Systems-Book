t=0:0.001:5; %Dominio
%misma base, diferente exponente
a=2;
b1=1/3;
b2=1/2;
b3=2;
b4=3;
y1=a.^(t*b1); 
y2=a.^(t*b2);
y3=a.^(t*b3);
y4=a.^(t*b4); 
subplot(2,2,1),plot(t,y1), title('Exponente=', num2str(b1))
subplot(2,2,2),plot(t,y2), title('Exponente=', num2str(b2))
subplot(2,2,3),plot(t,y3), title('Exponente=', num2str(b3))
subplot(2,2,4),plot(t,y4), title('Exponente=', num2str(b4))
