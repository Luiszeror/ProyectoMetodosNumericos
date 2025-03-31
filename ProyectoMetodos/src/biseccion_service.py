from flask import Flask, jsonify, request, render_template
from sympy import parse_expr
from methods.biseccion import biseccion_main
from Graphics import Graphics

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/api/biseccion', methods=['POST'])
def biseccion():
    data = request.get_json()
    function = data['function']
    xi = data.get('xi')
    xu = data.get('xu')

    expr = parse_expr(function)
    result = biseccion_main(expr, xi, xu)

    message = result.get('message')
    
    if result.get('divergence'):
        return jsonify({"message": message, "alert_error": True})
    
    plotter = Graphics(expr)
    
    try:
        graph_data = plotter.graph_biseccion(xi, xu, result['approximations'])
    except Exception as e:
        return jsonify({"message": "Error al generar la gráfica", "error": str(e)})

    return jsonify({
        "message": "Datos de Bisección procesados correctamente",
        "result": result,
        "graph_data" : graph_data
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
