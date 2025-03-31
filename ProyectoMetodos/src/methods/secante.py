from sympy import symbols, diff, E, nan, sqrt

x, xo = symbols('x xo')

def secante_main(F, x0, x1):
    print(F, x0, x1)
    FO = F.subs(x, xo)

    approximations = []
    divergence = True
    error = 10**-9
    cont = 1
    message = ""
    
    while True:
        gx_expr = x - (F * (x - xo)) / (F - FO)
        
        gx = gx_expr.subs({x: x1, xo: x0}).evalf()

        dgx_expr = diff(gx_expr, x)

        dgx = abs(dgx_expr.subs({x: x1, xo: x0}).evalf()) 
        
     
        print("Iter", cont , ": \ng(x)" , gx, "    g(x)'", dgx)

        if gx == nan or dgx == nan or gx.is_infinite or dgx.is_infinite:
            message = "La función evaluada tiene una singularidad, no se puede continuar"
            break
        else:
            approximations.append(float(gx))
        
        #elif (error > abs(x1 - x0) or abs(F.subs(x, x0).evalf()) <= error):
            
        if (error > abs(gx - x1) or abs(F.subs(x, x1).evalf()) <= error):
            divergence = False
            break
        else:   
            x0 = x1
            x1 = gx
        
        cont += 1
        
        if(cont > 200):
            message = "Después de 200 iteraciones, la función no está logrando converger a un punto."
            break

    return {
        "iterations": cont,
        "approximations": approximations,
        "divergence": divergence,
        "message": message
    }