%Cálcula la potencia de una señal senoidal con periodo de 2 segundos y sin desfase.
t=0:0.001:2; %Dominio
A=1; %Amplitud
T=2; %Periodo
theta=0; %fase
y=sin((2*pi/T)*t+theta); %funcion senoidal
P=sum(y.^2)/length(y); %La integral se aproxima como una suma promediada
