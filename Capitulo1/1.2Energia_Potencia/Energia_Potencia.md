# Capitulo 1, Conceptos Básicos
## Energía y Potencia

La energía de una señal se define de la siguiente manera

$$ E=\int_{-\infty}^{\infty}|x(t)|^{2}dt $$

donde |⋅| es la función valor absoluto. Para una señal periódica, su energía es un valor infinito. La potencia de una señal, por otro lado, se define como

$$ P=\frac{1}{T}\int_{T}\left|x(t)\right|^{2}dt$$

Esta última cantidad está definida para señales periódica. Para señales no periódica, su potencia es 0, dado que su periodo es infinito.

## Ejemplo teórico Potencia

Determine la potencia y energía de una señal senoidal x(t)=sin⁡(2π/T t).
Aplicando la definición de potencia anteriormente dado
$$P=\frac{1}{T}\int_{0}^{T}sin^2⁡(2\pi/T t)dt$$
Utilizando la identidad del ángulo doble se obtiene la siguiente expresión  
$$P=\frac{1}{T}\int_{0}^{T}\frac{1-cos(4\pi/T t)}{2}dt$$
Separando las integrales, la función anterior se puede escribir de la siguiente manera
$$P=\frac{1}{T}\int_{0}^{T}\frac{1}{2}-\frac{1}{T}\int_{0}^{T}\frac{cos(4\pi/T t)}{2}dt$$
La primera integral es simplemente la integral de una constante, mientras que la segunda integral es cero, dado que estamos integrando sobre dos ciclos completos. Por tanto
P=1/2

La energía de una señal senoidal es infinita.

## Ejemplo teórico Energia

Calcule la potencia y energía de una señal que está definida de la siguiente forma

$$x=\left\{\begin{matrix}
\\ 
2t, 0<=t<=1\\
0, para \ otros
\end{matrix}\right.$$

Aplicando la definción de energía, se obtiene
$$ E=\int_{0}^{1}\left| 2t \right|^2dt $$

Desarrollando la integral

$$ E=\frac{4}{3}t^{3}|_0^{1}=\frac{4}{3} $$

La potencia de esta señal es cero, dado que su periodo T tiende a infinito  (es una señal aperiódica) 

## Ejercicio para pensar

- En la vida real, existen señales periódicas? Qué implicaría la existencia de una señal periódica en términos de energía?
- Cómo se puede obtener una señal de potencia infinita? Sería posible esto en la vida real? 

