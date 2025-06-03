from sympy import symbols, lambdify, E
import numpy as np
import math

x = symbols('x')


def simpson_main(expr, a, b, n):
    if n % 2 != 0:
        return {
            "ptos_x": [],
            "ptos_fx": [],
            "solution": None,
            "divergence": True,
            "message": "El número de subintervalos (n) debe ser par para aplicar la regla de Simpson.",
        }

    divergence = False
    message = ""

    f = lambdify(x, expr, 'numpy')

    h = (b - a) / n  # Longitud de cada subintervalo
    suma = f(a) + f(b)  # Extremos de la integral

    xs = [a]
    fxs = [float(f(a))]

    x0 = a
    for i in range(1, n):
        xi = x0 + h
        xs.append(xi)
        fxs.append(float(f(xi)))

        # Alterna entre 4 y 2 según la posición del punto
        coef = 4 if i % 2 != 0 else 2
        suma += coef * f(xi)

        x0 = xi

    xs.append(b)
    fxs.append(float(f(b)))

    solution = abs(float(h / 3 * suma))

    # Control de desbordamiento
    if math.isinf(solution) or math.isnan(solution):
        divergence = True
        message = "Error de desbordamiento detectado, ingresar valores apropiados."

    return {
        "ptos_x": xs,
        "ptos_fx": fxs,
        "solution": solution,
        "divergence": divergence,
        "message": message,
    }


def prueba():
    f = E ** (x ** 4)
    a = -1
    b = 1
    n = 6  # Debe ser par para la regla de Simpson
    print(simpson_main(f, a, b, n))

# prueba()