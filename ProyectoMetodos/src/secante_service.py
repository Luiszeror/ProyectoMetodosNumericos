from flask import Flask, jsonify, request, render_template
from sympy import parse_expr
from methods.secante import secante_main
from Graphics import Graphics
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/api/secante', methods=['POST'])
def secante():
    data = request.get_json()
    function = data['function']
    
    x0 = data.get('x0_sec')
    x1 = data.get('x1_sec')
    
    expr = parse_expr(function)
    result = secante_main(expr, x0, x1)

    message = result.get('message')
    
    if result.get('divergence'):
        return jsonify({"message": message, "alert_error": True})

    plotter = Graphics(expr)
    
    try:
        graph_data = plotter.graph_secante(result['approximations'])
    except Exception as e:
        return jsonify({"message": "Error al generar la gráfica", "error": str(e)})

    return jsonify({
        "message": "Datos de Secante procesados correctamente",
        "result": result,
        "graph_data" : graph_data
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
