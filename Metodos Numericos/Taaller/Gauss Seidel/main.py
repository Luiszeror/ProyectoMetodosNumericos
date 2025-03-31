import numpy as np


A=np.array([4,0,-0.33,0], [-2,5,0,-0.33],[0,3.33,9,-1.5], [-0.66,0,2,6])
B =([0.5,0.25,0.16,0.33])
x0=np.zeros(4)

tolera = 0.00001
iteramax = 100

tamano = np.shape(A)
n = tamano[0]
m = tamano[1]

X = np.copy(X0)
diferencia = np.ones(n, dtype=float)
errado = 2 * tolera

itera = 0
while not (errado <= tolera or itera > iteramax):
    # por fila
    for i in range(0, n, 1):

        suma = 0
        for j in range(0, m, 1):

            if (i != j):
                suma = suma - A[i, j] * X[j]

        nuevo = (B[i] + suma) / A[i, i]
        diferencia[i] = np.abs(nuevo - X[i])
        X[i] = nuevo
    errado = np.max(diferencia)
    itera = itera + 1


X = np.transpose([X])


if (itera > iteramax):
    X = 0

verifica = np.dot(A, X)


print('respuesta X: ')
print(X)
print('verificar A.X=B: ')
print(verifica)