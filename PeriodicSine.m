%Implemente el siguiente código en Matlab para graficar una señal con una amplitud de 10, un periodo de 2, y un ángulo de desfase de 45 grados

t=0:0.001:10; %Dominio

A=10; %Amplitud

T=2; %Periodo

theta=pi/4; %fase

y=sin((2*pi/T)*t+theta); %funcion senoidal

plot(t,y), grid on 
