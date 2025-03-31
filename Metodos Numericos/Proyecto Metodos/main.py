# from fixed_point import fixed_point
# from bisection import bisection
# from secant import secant
# from trapezoidal import trapezoidal
# from simpson import simpson
# from gauss_seidel import gauss_seidel
import matplotlib.pyplot as plt

from bisection import bisection
from fixed_point import fixed_point
from gauss_seidel import gauss_seidel
from secant import secant
from simpson import simpson
from trapezoidal import trapezoidal


def main():
    while True:
        print("Seleccione un método numérico:")
        print("1. Punto fijo")
        print("2. Bisección")
        print("3. Secante")
        print("4. Trapecio")
        print("5. Simpson")
        print("6. Gauss-Seidel")
        print("7. Salir")
        option = input("Ingrese una opción: ")
        if option == "1":
            function = input("Ingrese la función: ")
            initial_value = float(input("Ingrese el valor inicial: "))
            error = float(input("Ingrese el porcentaje de error: "))
            root, error_percent, graph = fixed_point(function, initial_value, error)
            print(f"La raíz es: {root}")
            print(f"El porcentaje de error es: {error_percent}")
            plt.show(graph)
        elif option == "2":
            function = input("Ingrese la función: ")
            x0 = float(input("Ingrese el valor de X0: "))
            x1 = float(input("Ingrese el valor de X1: "))
            error = float(input("Ingrese el porcentaje de error: "))
            approx, error_percent, graph = bisection(function, x0, x1, error)
            print(f"El resultado aproximado es: {approx}")
            print(f"El porcentaje de error es: {error_percent}")
            plt.show(graph)
        elif option == "3":
            function = input("Ingrese la función: ")
            x0 = float(input("Ingrese el valor de X0: "))
            x1 = float(input("Ingrese el valor de X1: "))
            error = float(input("Ingrese el porcentaje de error: "))
            approx, error_percent, graph = secant(function, x0, x1, error)
            print(f"El resultado aproximado es: {approx}")
            print(f"El porcentaje de error es: {error_percent}")
            plt.show(graph)
        elif option == "4":
            function = input("Ingrese la función: ")
            lower_limit = float(input("Ingrese el límite inferior: "))
            upper_limit = float(input("Ingrese el límite superior: "))
            intervals = int(input("Ingrese el número de intervalos: "))
            approx, error_percent, graph = trapezoidal(function, lower_limit, upper_limit, intervals)
            print(f"El resultado aproximado es: {approx}")
            print(f"El porcentaje de error es: {error_percent}")
            plt.show(graph)
        elif option == "5":
            function = input("Ingrese la función: ")
            lower_limit = float(input("Ingrese el límite inferior: "))
            upper_limit = float(input("Ingrese el límite superior: "))
            intervals = int(input("Ingrese el número de intervalos (debe ser par): "))
            if intervals % 2 != 0:
                print("El número de intervalos debe ser par.")
                continue
            approx, error_percent, graph = simpson(function, lower_limit, upper_limit, intervals)
            print(f"El resultado aproximado es: {approx}")
            print(f"El porcentaje de error es: {error_percent}")
            plt.show(graph)
        elif option == "6":
            functions = input("Ingrese las funciones separadas por comas: ")
            coefficients = input("Ingrese los coeficientes separados por comas: ")
            index = int(input("Ingrese el índice del vector de independientes: "))
            initial_guess = input("Ingrese el vector de la solución inicial separado por comas: ")
            functions = functions.split(",")
            coefficients = [list(map(float, c.split())) for c in coefficients.split(",")]
            independent = list(map(float, independent.split(",")))
            initial_guess = list(map(float, initial_guess.split(",")))
            approx, graph = gauss_seidel(functions, coefficients, independent, initial_guess=initial_guess)
            print(f"El resultado aproximado es: {approx}")
            plt.show(graph)
            # approx, graph = gauss_seidel(functions, coefficients, index)
            # print(f"El resultado aproximado es: {approx}")
            # plt.show(graph)
        elif option == "7":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
