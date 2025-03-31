

A =[[]]     
b = []

#función encargada de validar que el formato ingresado sea correcto, 
# y de separar la entrada de la matriz tipo string hacia la matriz A y el vector b
def estructure_matriz(matriz_str, nVar):
     
    try:
        # Convertir la cadena de texto a la matriz A completa
        matriz = [
            [float(num) for num in row.split(',')]
            for row in matriz_str.split('\n') if row.strip()
        ]

        #validacion del tamaño de la matriz
        if len(matriz) != nVar or any(len(row) != nVar + 1 for row in matriz):
            return 1

        else: 
            b.clear() #se vacia b
            
            # Extraer la última columna de matriz y asignarla a b
            for row in matriz:
                b.append(row.pop())  # Extrae y elimina el último elemento de cada fila
            
        
            A.clear()  #se vacia A
            A.extend(matriz)
            print(len(A))      
            print("Matriz A:", A)
            print("Vector b:", b)
            return 2
    except ValueError as e:
        return 0
   
def jacobi_main(matriz_str, nVar):
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
            message = "El tipo de formato ingresado es invalido"
        if response == 1:
            message = "La cantidad de elementos de la matriz es incorrecta segun el número de coeficientes"      
    else:
        print(A)
        Al = len(A)
        x0 = [0] * Al  # Vector de soluciones iniciales según el tamaño de A
        x = [0] * Al  # Vector temporal para los nuevos valores según el tamaño de A
               
        while cont <= 200:
            for i in range(Al):
                suma = 0
                for j in range(Al):
                    # Se ignora el elemento en la diagonal para que cada nueva aproximación de xi​ 
                    # dependa solo de los valores de otras variables y no de sí mismo
                    if j != i:  
                        suma += A[i][j] * x0[j]  
                if(A[i][i]!=0):
                    x[i] = (b[i] - suma) / A[i][i]
                else:
                    cero_exp = True
                    break;       
               
            if cero_exp:
                message = "La diagonal no puede contener coeficientes iguales a cero." 
                break;
            approximations.append(x[:])

            if all(abs(x[i] - x0[i]) < error for i in range(Al)):
                print("Solución aproximada:", x)

                solution = approximations[-1] if approximations else None
                divergence = False
                break
            
            for i in range(Al): # se actualiza el vector anterior x0
                x0[i] = x[i]
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