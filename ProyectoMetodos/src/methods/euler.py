


from sympy import symbols

def euler_main(f, x0, y0, h, n):
    if h <= 0:
        raise ValueError("El paso h debe ser mayor que cero.")
    if n <= 0:
        raise ValueError("El número de pasos n debe ser mayor que cero.")

    x_vals = [x0]
    y_vals = [y0]
    errores = []
    x, y = x0, y0

    for i in range(n):
        try:
            dy = f(x, y)
        except Exception as e:
            raise RuntimeError(f"Error al evaluar f({x}, {y}): {e}")

        y_nuevo = y + h * dy
        x_nuevo = x + h

        error = abs(y_nuevo - y)
        errores.append(error)

        x_vals.append(x_nuevo)
        y_vals.append(y_nuevo)

        x, y = x_nuevo, y_nuevo

    return {
        "x": x_vals,
        "y": y_vals,
        "errors": errores,
        "n": n,
        "h": h
    }

# === Test local ===
def test():
    from sympy import symbols, lambdify
    x, y = symbols('x y')
    f_expr = x + y
    f_lambda = lambdify((x, y), f_expr, modules=['math'])

    x0 = 0
    y0 = 1
    h = 0.1
    n = 10

    resultado = euler_main(f_lambda, x0, y0, h, n)
    print(resultado)

# test()

