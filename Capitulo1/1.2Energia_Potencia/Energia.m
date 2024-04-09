t=0:0.001:1; %Dominio
y=2*t; %funcion senoidal
E=sum(y.^2)/length(y); %La integral se aproxima como una suma promediada
