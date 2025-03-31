import numpy as np


def estructure_matriz(matriz_str, nVar):
    """
    Estructura la matriz A y el vector b a partir de una cadena de texto.
    
    Parámetros:
    - matriz_str: Cadena con las filas de la matriz separadas por saltos de línea.
    - nVar: Número de variables (dimensiones de la matriz).

    Retorna:
    - (A, b): Matriz de coeficientes y vector independiente.
    - status: Código de estado (0: error, 1: tamaño incorrecto, 2: éxito).
    """
    try:
        # Convertir la cadena de texto en una lista de filas
        matriz = [
            [float(num) for num in row.split(',')]
            for row in matriz_str.strip().split('\n') if row.strip()
        ]

        # Validar que la matriz tiene el tamaño adecuado
        if len(matriz) != nVar or any(len(row) != nVar + 1 for row in matriz):
            return None, None, 1

        # Separar A y b
        A = [row[:-1] for row in matriz]  # Todo excepto la última columna
        b = [row[-1] for row in matriz]  # Última columna
        return A, b, 2
    except ValueError:
        return None, None, 0


def broyden_main(f, jacobian, x_init, tol=1e-15, max_iter=200):
    """
    Método de Broyden para resolver sistemas de ecuaciones no lineales.
    
    Parámetros:
    - f: Función que representa el sistema de ecuaciones no lineales.
    - jacobian: Función que calcula el Jacobiano inicial (puede ser aproximado).
    - x_init: Solución inicial (vector).
    - tol: Tolerancia para la convergencia.
    - max_iter: Número máximo de iteraciones.

    Retorna:
    - Diccionario con el número de iteraciones, la solución y detalles.
    """
    x = np.array(x_init, dtype=float)  # Vector inicial como arreglo de NumPy
    approximations = [x.tolist()]  # Lista para guardar las aproximaciones
    iter_count = 0
    divergence = False
    message = ""

    try:
        # Inicializar el Jacobiano inverso
        J_inv = np.linalg.inv(jacobian(x))

        while iter_count < max_iter:
            fx = f(x)  # Evaluar la función en x
            delta_x = -J_inv.dot(fx)  # Calcular la actualización
            x_new = x + delta_x  # Nueva aproximación

            # Guardar la aproximación
            approximations.append(x_new.tolist())

            # Verificar la convergencia
            if np.linalg.norm(delta_x) < tol:
                message = "Convergencia alcanzada."
                break

            # Actualizar el Jacobiano con la fórmula de Broyden
            delta_fx = f(x_new) - fx
            delta_x = x_new - x
            J_inv += np.outer((delta_x - J_inv.dot(delta_fx)), delta_x) / np.dot(delta_x, delta_fx)

            # Actualizar x y contar iteraciones
            x = x_new
            iter_count += 1

        if iter_count == max_iter:
            divergence = True
            message = "No convergió después del máximo de iteraciones."
    except np.linalg.LinAlgError:
        divergence = True
        message = "Error en la inversión del Jacobiano inicial."

    return {
        "iterations": iter_count,
        "approximations": approximations,
        "solution": x.tolist(),
        "divergence": divergence,
        "message": message,
    }


# Ejemplo de uso
if __name__ == "__main__":
    # Entrada de prueba para `estructure_matriz`
    matriz_str = "3,2,-4,3\n2,3,3,15\n5,-3,1,14"
    nVar = 3
    A, b, status = estructure_matriz(matriz_str, nVar)

    if status == 2:
        print("Matriz estructurada correctamente:")
        print("A:", A)
        print("b:", b)
    elif status == 1:
        print("Error: Tamaño de la matriz incorrecto.")
    else:
        print("Error: Formato inválido.")

    # Funciones de prueba para `broyden_main`
    def f(x):
        return np.array([
            x[0] ** 2 + x[1] ** 2 - 1,
            x[0] - x[1] ** 3
        ])

    def jacobian(x):
        return np.array([
            [2 * x[0], 2 * x[1]],
            [1, -3 * x[1] ** 2]
        ])

    x_init = [0.5, 0.5]
    result = broyden_main(f, jacobian, x_init)
    print("\nResultados del método de Broyden:")
    print(result)
