# Algoritmo para resolver ecuaciones a través
# del método del punto fijo

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función
def puntofijo(gx, a, tolera, iteramax=15):# Inicio de la función
    i = 1  # Contador de iteraciones
    b = gx(a)
    tramo = abs(b - a)
    while (tramo >= tolera and i <= iteramax):
        a = b
        b = gx(a)
        tramo = abs(b - a)
        i = i + 1
    respuesta = b # Retorno de la función

    # Validar respuesta
    if (i >= iteramax):
        respuesta = np.nan
    return (respuesta)
# Fin de la función

# ENTRADAS
fx = lambda x: 2*(x**2) - x - 5
gx = lambda x: np.sqrt((x+5)/2)

a = -5  # intervalo
b = 5
tolera = 0.0001
iteramax = 15  # máximo de iteraciones
muestras = 11  # gráfico
tramos = 50

# PROCEDIMIENTO
respuesta = puntofijo(gx, a, tolera)
xi = np.linspace(a,b,muestras)
fi = fx(xi)
gi = gx(xi)
yi = xi

# SALIDAS
print(respuesta)
plt.plot(xi,fi, label='f(x)')
plt.plot(xi,gi, label='g(x)')
plt.plot(xi,yi, label='y=x')
plt.plot(respuesta,0, 'ro', label='raíz')

if (respuesta!= np.nan):
    plt.axvline(respuesta)#Línea vertical donde cruzan la función idéntica y el g(x)
    #z=9
plt.axhline(0, color='k')
plt.axhline(0, 0,color='k')
plt.title('Punto Fijo')
plt.legend()
plt.show()