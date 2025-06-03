from flask import Flask, request, jsonify, render_template
from sympy import symbols, sympify, lambdify
from methods.euler import euler_main
from Graphics import Graphics

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/euler', methods=['POST'])
def resolver_euler():
    data = request.get_json()

    expresion = data.get("expresion")
    if expresion is None or not isinstance(expresion, str) or expresion.strip() == "":
        return jsonify({"error": "No se recibió una expresión válida para f(x, y)."}), 400

    try:
        x0 = float(data.get("x0", 0))
        y0 = float(data.get("y0", 0))
        h = float(data.get("h", 0.1))
        n = int(data.get("n", 10))
    except Exception:
        return jsonify({"error": "Los parámetros numéricos x0, y0, h o n no son válidos."}), 400

    x, y = symbols('x y')
    try:
        expresion = expresion.replace("^", "**")
        f_expr = sympify(expresion)
        f_lambda = lambdify((x, y), f_expr, modules=['math'])
    except Exception as e:
        return jsonify({"error": f"Error al interpretar la expresión: {str(e)}"}), 400

    try:
        puntos = euler_main(f_lambda, x0, y0, h, n)

        # Obtener valores
        x_vals = puntos["x"]
        y_vals = puntos["y"]
        y_real = puntos.get("y_real", [])  # Solo si tienes la solución exacta

        g = Graphics(f_expr)

        # Si tienes la solución exacta, pásala también
        if y_real:
            graph_data = g.graph_euler(x_vals, y_vals, y_real)
        else:
            graph_data = g.graph_euler(x_vals, y_vals)

        return jsonify({
            "resultado": puntos,
            "graph_data": graph_data
        })

    except Exception as e:
        return jsonify({"error": f"Error al ejecutar Euler: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
