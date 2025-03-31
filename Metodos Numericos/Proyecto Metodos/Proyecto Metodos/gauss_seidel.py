from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt

def gauss_seidel(functions: List[str], coefficients: List[List[float]], independent: List[float], initial_guess: List[float]) -> Tuple[List[float], List[float], List[List[float]]]:
    """
    This function solves a system of linear equations using the Gauss-Seidel method.
    :param functions: A list of strings representing the equations in the system.
    :param coefficients: A list of lists representing the coefficients of the variables in each equation.
    :param independent: A list representing the independent values in the system.
    :param initial_guess: A list representing the initial guess for the solution.
    :return: A tuple containing the solution, the error percentage, and the graph of the solution.
    """
    n = len(independent)
    x = np.array(initial_guess)
    error = 1
    error_percent = []
    iterations = 0
    graph = []
    while error > 0.01:
        x_new = np.zeros(n)
        for i in range(n):
            s1 = sum(coefficients[i][j] * x_new[j] for j in range(i))
            s2 = sum(coefficients[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (independent[i] - s1 - s2) / coefficients[i][i]
        error = np.linalg.norm(x_new - x) / np.linalg.norm(x_new)
        error_percent.append(error)
        x = x_new
        iterations += 1
        graph.append(list(x))
    return list(x), error_percent, graph

# Define los argumentos necesarios
functions = ['2*x1 - x2 - x3 = 0', '-x1 + 2*x2 - x3 = 0', '-x1 - x2 + 2*x3 = 0']
coefficients = [[2, -1, -1], [-1, 2, -1], [-1, -1, 2]]
independent = [0, 0, 0]
initial_guess = [0, 0, 0]

# Llamar a la función gauss_seidel
solution, error_percent, graph = gauss_seidel(functions, coefficients, independent, initial_guess)

# Crear una lista de los números de iteración
iterations = list(range(1, len(graph) + 1))

# Crear un gráfico para cada variable
for i in range(len(graph[0])):
    variable_values = [x[i] for x in graph]
    plt.plot(iterations, variable_values, label=f'x{i+1}')


# Create a list of the iteration numbers
iterations = list(range(1, len(graph) + 1))

# Create a plot for each variable
for i in range(len(graph[0])):
    variable_values = [x[i] for x in graph]
    plt.plot(iterations, variable_values, label=f'x{i+1}')

# Add labels and legend to the plot
plt.xlabel('Iteration')
plt.ylabel('Variable Value')
plt.title('Gauss-Seidel Method')
plt.legend()

# Show the plot
plt.show()