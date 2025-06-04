from sympy import symbols, diff, E, nan, sqrt
import math

x, xo = symbols('x xo')

def is_valid_number(value):
    """Verifica si un número es real, no NaN ni infinito."""
    if isinstance(value, complex):
        return value.imag == 0 and not math.isnan(value.real) and not math.isinf(value.real)
    return not math.isnan(value) and not math.isinf(value)

def secante_main(F, x0, x1):

    try:
    # Validación inicial de la función
        test_val = F.subs(x, x0).evalf()
        if not is_valid_number(float(test_val)):
            return {
                "iterations": 0,
                "approximations": [],
                "divergence": True,
                "message": "La función no es válida en el punto inicial. Verifica dominio (división por cero, raíces de negativos, etc)."
            }
    except Exception as e:
        return {
            "iterations": 0,
            "approximations": [],
            "divergence": True,
            "message": f"No se pudo evaluar la función inicial: {str(e)}"
    }
    print(F, x0, x1)
    FO = F.subs(x, xo)

    approximations = []
    divergence = True
    error = 10**-9
    cont = 1
    message = ""
    
    while True:
        try:
            gx_expr = x - (F * (x - xo)) / (F - FO)
            gx = gx_expr.subs({x: x1, xo: x0}).evalf()

            dgx_expr = diff(gx_expr, x)
            dgx = abs(dgx_expr.subs({x: x1, xo: x0}).evalf())
        except Exception as e:
            message = f"Error durante la evaluación de la función: {str(e)}"
            break

        print("Iter", cont , ": \ng(x)" , gx, "    g(x)'", dgx)

        # Validar gx y dgx
        if gx.is_real and dgx.is_real:
            gx_f = float(gx)
            dgx_f = float(dgx)
        else:
            message = "La función evaluada devolvió un número complejo. Verifica la expresión o el dominio."
            break

        if not is_valid_number(gx_f) or not is_valid_number(dgx_f):
            message = "La función evaluada tiene una singularidad (NaN o infinito), no se puede continuar."
            break
        else:
            approximations.append(gx_f)

        # Verificar convergencia
        if (error > abs(gx_f - x1) or abs(F.subs(x, x1).evalf()) <= error):
            divergence = False
            break
        else:
            x0 = x1
            x1 = gx_f

        cont += 1

        if cont > 200:
            message = "Después de 200 iteraciones, la función no está logrando converger a un punto."
            break

    return {
        "iterations": cont,
        "approximations": approximations,
        "divergence": divergence,
        "message": message
    }
