from flask import Flask, request, jsonify, render_template
from sympy import symbols, sympify, lambdify
from methods.euler import euler_main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/api/euler', methods=['POST'])
def resolver_euler():
    data = request.get_json()

    # Extraer y validar datos del request
    expresion = data.get("expresion")  # f(x, y) como string

    if expresion is None or not isinstance(expresion, str) or expresion.strip() == "":
        return jsonify({"error": "No se recibió una expresión válida para f(x, y)."}), 400

    x0 = float(data.get("x0", 0))
    y0 = float(data.get("y0", 0))
    h = float(data.get("h", 0.1))
    n = int(data.get("n", 10))

    # Crear función f(x, y) con sympy
    x, y = symbols('x y')
    try:
        # Reemplazar potencias escritas con ^ por **
        expresion = expresion.replace("^", "**")
        f_expr = sympify(expresion)
        f_lambda = lambdify((x, y), f_expr, modules=['math'])
    except Exception as e:
        return jsonify({"error": f"Error al interpretar la expresión: {str(e)}"}), 400

    # Calcular solución con Euler
    try:
        puntos = euler_main(f_lambda, x0, y0, h, n)
        return jsonify({"resultado": puntos})
    except Exception as e:
        return jsonify({"error": f"Error al ejecutar Euler: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
