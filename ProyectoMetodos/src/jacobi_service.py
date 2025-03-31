from flask import Flask, jsonify, request, render_template
from methods.jacobi import jacobi_main
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/api/jacobi', methods=['POST'])
def jacobi():
    data = request.get_json()
  
    matriz_str = data.get('matriz_jac')
    nVar = data.get('nVar_jac')
   
    result = jacobi_main(matriz_str, nVar)
    
    message = result.get('message')
    
    if result.get('divergence'):
        return jsonify({"message": message, "alert_error": True})

    solution = result.get('solution')
    
    if solution:
        formatted_solution = ", ".join(f"{value:.4f}" for value in solution)
        
    return jsonify({
        "message": "Datos del método Jacobi procesados correctamente",
        "matriz" : result,
        "solution": formatted_solution
    })
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
