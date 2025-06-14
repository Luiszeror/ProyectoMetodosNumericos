from sympy import symbols, lambdify, E
import numpy as np
import math

x = symbols('x')


def trapecio_main(expr, a, b, n):
    divergence = False
    message = ""

    f = lambdify(x, expr, 'numpy')

    h = (b - a) / n
    suma = 0.5 * (f(a) + f(b))

    xs = [a]
    fxs = [float(f(a))]
    areas_individuales = []

    x0 = a
    for i in range(1, n):
        xi = x0 + h
        xs.append(xi)
        fxs.append(float(f(xi)))
        suma += f(xi)

        area_trapecio = h * (f(x0) + f(xi)) / 2
        areas_individuales.append(float(area_trapecio))

        x0 = xi

    xs.append(b)
    fxs.append(float(f(b)))

    area_ultimo = h * (f(x0) + f(b)) / 2
    areas_individuales.append(float(area_ultimo))

    solution = abs(float(h * suma))
    # control overFlow
    if math.isinf(solution) or math.isnan(solution):
        divergence = True
        message = "Error de desbordamiento detectado, ingresar valores apropiados"

    return {
        "ptos_x": xs,
        "ptos_fx": fxs,
        "areas_individuales": areas_individuales,  # Nuevo campo
        "solution": solution,
        "divergence": divergence,
        "message": message,
    }


def prueba():
    f = E ** (x ** 4)
    a = -1
    b = 1
    n = 5
    print(trapecio_main(f, a, b, n))
# prueba()