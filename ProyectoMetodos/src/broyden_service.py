from flask import Flask, jsonify, request, render_template
import numpy as np
from methods.broyden import broyden_main

app = Flask(__name__)


def f(x):
    return np.array([
        x[0]**2 + x[1]**2 - 1, 
        x[0] - x[1]**3          
    ])

def jacobian(x):
    return np.array([
        [2 * x[0], 2 * x[1]],   
        [1, -3 * x[1]**2]      
    ])

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/api/broyden', methods=['POST'])
def broyden():
    data = request.get_json()
  

    matriz_str = data.get('matriz_bro')
    nVar = data.get('nVar_bro')
    x_init = data.get('x_init', [0.5, 0.5])  

   
    if not matriz_str or not nVar:
        return jsonify({
            "message": "Datos incompletos. Se requiere 'matriz_bro' y 'nVar_bro'.",
            "alert_error": True
        }), 400

    try:
        
        result = broyden_main(f, jacobian, x_init)

        message = result.get('message')

        
        if result.get('divergence'):
            return jsonify({
                "message": message,
                "alert_error": True
            }), 500

      
        solution = result.get('solution')
        formatted_solution = ", ".join(f"{value:.4f}" for value in solution) if solution else "Sin solución"

        return jsonify({
            "message": "Datos del método Broyden procesados correctamente.",
            "matriz": result,
            "solution": formatted_solution
        })

    except Exception as e:
        return jsonify({
            "message": f"Error procesando el método Broyden: {str(e)}",
            "alert_error": True
        }), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
