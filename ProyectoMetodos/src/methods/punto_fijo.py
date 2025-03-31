from sympy import symbols

x = symbols('x')

def punto_fijo_main(expr, xi):
    
    iterations = []
    approximations = []
    errors = []
    cont = 0
    divergence = False   
    error = 1

    while error > 10**-9:
        cont += 1
        
        gx = float(expr.subs(x, xi).evalf())

        if cont > 1:
            error = abs((gx - xi) / gx) 
        
            if errors and error > errors[-1]: 
                divergence = True
                break

            errors.append(error)
    
        approximations.append(gx)
        iterations.append(cont)

        xi = gx

    
   
    return {
        "iterations": iterations,
        "approximations": approximations,
        "errors": errors,
        "divergence": divergence
    }

def test():
    #T = sqrt( (x+5) /2)  
    T = 2*x**2 - 5
    xi = 2  
    result = punto_fijo_main(T, xi)
    print(result)

#test()