from flask import Flask, jsonify, request, render_template
from sympy import parse_expr
from methods.newton import newton_main
from Graphics import Graphics
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/api/newton', methods=['POST'])
def newton():
    data = request.get_json()
    function = data['function']
    
    xo = data.get('xo_newton')
    expr = parse_expr(function)

    result = newton_main(expr, xo)

    message = result.get('message')
    
    if result.get('divergence'):
        return jsonify({"message": message, "alert_error": True})

    plotter = Graphics(expr)

    try:
        graph_data = plotter.graph_newton(result['approximations'], xo)
    except Exception as e:
        return jsonify({"message": "Error al generar la gráfica", "error": str(e)})
    


    return jsonify({
        "message": "Datos de Newton-Rhapson procesados correctamente",
        "result": result,
        "graph_data" : graph_data    
    })
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
