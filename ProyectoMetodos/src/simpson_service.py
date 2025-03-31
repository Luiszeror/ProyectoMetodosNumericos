from flask import Flask, jsonify, request, render_template
from sympy import parse_expr
from methods.simpson import simpson_main
from Graphics import Graphics

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/api/simpson', methods=['POST'])
def simpson():
    data = request.get_json()
    function = data['function']
    
    expr = parse_expr(function)
   
    a = data.get('a_simp')
    b = data.get('b_simp')
    num = data.get('num_simp')
   
    result = simpson_main(expr,a,b,num)
    
    message = result.get('message')
    
    if result.get('divergence'):
        return jsonify({"message": message, "alert_error": True})

    solution = result.get('solution')

    plotter = Graphics(expr)

    try:
        graph_data = plotter.graph_simpson(result['ptos_x'], result['ptos_fx'], result['solution'])    
    except Exception as e:
        return jsonify({"message": "Error al generar la gráfica", "error": str(e)})
    
    return jsonify({
        "message": "Datos del método simpson procesados correctamente",
        "result": result,
        "graph_data" : graph_data,
        "solution": solution
    })
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
