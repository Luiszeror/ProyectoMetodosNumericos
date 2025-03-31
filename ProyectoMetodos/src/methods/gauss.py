
A = [[]]
b = []

# Función encargada de validar el formato y separar la matriz A y el vector b
def estructure_matriz(matriz_str, nVar):
    try:
        # Convertir la cadena de texto a la matriz A completa
        matriz = [
            [float(num) for num in row.split(',')]
            for row in matriz_str.split('\n') if row.strip()
        ]

        # Validación del tamaño de la matriz
        if len(matriz) != nVar or any(len(row) != nVar + 1 for row in matriz):
            return 1
        else: 
            b.clear()  # Vaciar b
            # Extraer la última columna de matriz y asignarla a b
            for row in matriz:
                b.append(row.pop())  # Extrae y elimina el último elemento de cada fila
            
            A.clear()  # Vaciar A
            A.extend(matriz)
            return 2
    except ValueError as e:
        return 0

# Método Gauss-Seidel
def gauss_main(matriz_str, nVar):
    approximations = []
    solution = []
    divergence = True
    message = ""
    error = 1e-15
    cont = 0
    cero_exp = False
    
    response = estructure_matriz(matriz_str, nVar)  
    if response != 2:     
        if response == 0:
            message = "El tipo de formato ingresado es inválido"
        if response == 1:
            message = "La cantidad de elementos de la matriz es incorrecta según el número de coeficientes"      
    else:
        print(A)
        Al = len(A)
        x = [0] * Al  # Vector de soluciones iniciales según el tamaño de A
        
        while cont <= 200:
            x_prev = x[:]  # Guardar el vector anterior para calcular el error
            for i in range(Al):
                suma = 0
                for j in range(Al):
                    if j != i:  # No sumar el elemento de la diagonal
                        suma += A[i][j] * x[j]  # Aquí se usa el valor actualizado de x[j]
                if A[i][i] != 0:
                    x[i] = (b[i] - suma) / A[i][i]
                else:
                    cero_exp = True
                    break
               
            if cero_exp:
                message = "La diagonal no puede contener coeficientes iguales a cero." 
                break
            approximations.append(x[:])

            # Verificar la convergencia
            if all(abs(x[i] - x_prev[i]) < error for i in range(Al)):
                print("Solución aproximada:", x)
                solution = approximations[-1] if approximations else None
                divergence = False
                break
            
            cont += 1

        if cont > 200:
            message = "Después de 200 iteraciones, la función no está logrando converger a un punto."

    return {
        "iterations": cont,
        "approximations": approximations,
        "solution" : solution,
        "divergence": divergence,
        "message": message,
    }

