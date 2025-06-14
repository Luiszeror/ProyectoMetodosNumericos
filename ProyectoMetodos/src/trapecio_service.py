from flask import Flask, jsonify, request, render_template
from sympy import parse_expr
from methods.trapecio import trapecio_main
from Graphics import Graphics

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/trapecio', methods=['POST'])
def jacobi():
    data = request.get_json()
    function = data['function']

    expr = parse_expr(function)

    a = data.get('a_trap')
    b = data.get('b_trap')
    num = data.get('num_trap')

    result = trapecio_main(expr, a, b, num)

    message = result.get('message')

    if result.get('divergence'):
        return jsonify({"message": message, "alert_error": True})

    solution = result.get('solution')
    areas_individuales = result.get('areas_individuales')

    plotter = Graphics(expr)

    try:
        graph_data = plotter.graph_trapecio(result['ptos_x'], result['ptos_fx'], result['solution'])
    except Exception as e:
        return jsonify({"message": "Error al generar la gráfica", "error": str(e)})

    return jsonify({
        "message": "Datos del método Trapecio procesados correctamente",
        "result": result,
        "graph_data": graph_data,
        "solution": solution,
        "areas_individuales": areas_individuales,  # Nuevo campo en la respuesta
        "detalle_trapecios": [
            {
                "trapecio": i+1,
                "intervalo": [result['ptos_x'][i], result['ptos_x'][i+1]],
                "altura": result['ptos_x'][i+1] - result['ptos_x'][i],
                "base_izq": result['ptos_fx'][i],
                "base_der": result['ptos_fx'][i+1],
                "area": areas_individuales[i]
            }
            for i in range(len(areas_individuales))
        ]
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)