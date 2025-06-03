from sympy import symbols, lambdify, sympify, exp

def euler_main(f, x0, y0, h, n):
    if h <= 0:
        raise ValueError("El paso h debe ser mayor que cero.")
    if n <= 0:
        raise ValueError("El número de pasos n debe ser mayor que cero.")

    x_vals = [x0]
    y_vals = [y0]
    errores = []
    y_real_vals = []

    # === Si conoces la solución exacta ===
    x_sym = symbols('x')
    y_exact_expr = 2 * exp(x_sym) - x_sym - 1  # ← Aquí defines tu solución exacta
    y_exact_func = lambdify(x_sym, y_exact_expr, modules=["math"])

    try:
        y_real_vals.append(y_exact_func(x0))  # valor real inicial
    except Exception:
        y_real_vals.append(None)

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

        try:
            y_real_vals.append(y_exact_func(x_nuevo))
        except Exception:
            y_real_vals.append(None)

        x, y = x_nuevo, y_nuevo

    return {
        "x": x_vals,
        "y": y_vals,
        "y_real": y_real_vals,
        "errors": errores,
        "n": n,
        "h": h
    }

# === Test local ===
def test():
    x, y = symbols('x y')
    f_expr = x + y
    f_lambda = lambdify((x, y), f_expr, modules=['math'])

    x0 = 0
    y0 = 1
    h = 0.1
    n = 10

    resultado = euler_main(f_lambda, x0, y0, h, n)
    print("x:", resultado["x"])
    print("y aproximada:", resultado["y"])
    print("y exacta:", resultado["y_real"])

# test()
