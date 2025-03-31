from sympy import symbols

x = symbols('x')

def function(xi, expr):
    return float(expr.subs(x, xi))

def biseccion_main(expr, xi, xu):
    xi = float(xi)  
    xu = float(xu)
    cont = 0
    error = 1
    xr = 0
    xr_ant = 0
    
    message = ""
    iterations = []
    approximations = []
    errors = []
    divergence = False 
    
    # Validación de intervalo inicial
    if function(xi, expr) * function(xu, expr) > 0:
        message =  "El intervalo [xi, xu] no contiene una raíz. Por favor ingrese valores diferentes de xi y xu."
        divergence = True
    else:   

        while error > 10**-9 and cont < 100:
            cont += 1
            xr_ant = xr
            xr = (xi + xu) / 2
            
            if function(xi, expr) * function(xr, expr) < 0:
                xu = xr
            else:
                xi = xr
            
            if cont > 1:
                error = abs((xr - xr_ant) / xr) if xr != 0 else 0
                errors.append(error)

                if error > errors[-1]: 
                    divergence = True

            iterations.append(cont)
            approximations.append(xr)

    return {
        "iterations": iterations,
        "approximations": approximations,
        "errors": errors,
        "divergence": divergence,
        "message": message
    }



def test():
    #F = sqrt( (x+5) /2)  
    F = -0.5*x**2 + 2.5*x + 4.5
    result = biseccion_main(F, 0, -20000)
    print(result)

#test()