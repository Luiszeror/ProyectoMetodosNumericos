from flask import Flask, jsonify, request, render_template
from sympy import parse_expr
from methods.punto_fijo import punto_fijo_main
from Graphics import Graphics
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/api/punto_fijo', methods=['POST'])
def punto_fijo():
    data = request.get_json()
    function = data['function']
    transf = data.get('transformada')
    xo = data.get('xo')

    expr = parse_expr(function)
    expr_transf = parse_expr(transf)

    result = punto_fijo_main(expr_transf, xo)

    if result.get('divergence'):
        return jsonify({"message": "La función diverge", "alert_error": True})

    plotter = Graphics(expr)

    try:
        graph_data = plotter.graph_punto_fijo(result['approximations'], xo)
    except Exception as e:
        return jsonify({"message": "Error al generar la gráfica", "error": str(e)})

    return jsonify({
        "message": "Datos de Punto Fijo procesados correctamente",
        "result": result,
        "graph_data" : graph_data    
        })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
