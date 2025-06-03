from flask import Flask, jsonify, request, render_template
from methods.gauss import gauss_main
app = Flask(__name__)



@app.route('/api/gauss', methods=['POST'])
def gauss():
    data = request.json  # Obtener JSON enviado por el frontend
    nVar = data.get("nVar_gau")
    matriz = data.get("matriz_gau")

    result = gauss_main(matriz, nVar)

    message = result.get('message')

    if result.get('divergence'):
        return jsonify({"message": message, "alert_error": True})

    solution = result.get('solution')
    print(solution)
    if solution:
        formatted_solution = ", ".join(f"{value:.4f}" for value in solution)



    return jsonify({
        "message": "Datos del método Gauss-Seidel procesados correctamente",
        "matriz" : result,
        "solution": formatted_solution
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

