from sympy import symbols, diff, E, nan, sqrt, sin

x = symbols('x')

def newton_main(F, xi):
    print(F , xi)
    
    approximations = []
    divergence = True 
    message = ""
    cont = 1
    error = 1*10**-9
    #errors = []
    
    while True:   
        
        gx = xi -(F / diff(F))
        
        gx = gx.subs(x, xi).evalf()
        
        dgx_expr = 1 - diff(F / diff(F))
        
        dgx = abs(dgx_expr.subs(x, xi).evalf())
        
        print("Iter",cont,":\ng(x):", gx, "\ng(x)':", dgx ,'\n')
        
        if gx == nan or dgx == nan or gx.is_infinite:
            message = "La función evaluada tiene una singularidad en x =", xi, "no se puede continuar"
            break        
        else:
            approximations.append(float(gx))   
            
        if dgx == 0:
            message = "La derivada en el punto x =",xi ,"es cero, no se puede continuar"
            break
                
        if(error > abs(gx - xi) or abs(F.subs(x, xi).evalf()) <= error):
            divergence = False
            break
        else:  
            #if(cont > 1):  
            #    errors.append( abs((gx-xi)/gx) )

            xi = gx
    
        cont += 1
        
        if(cont >200):
            message = "Después de 200 iteraciones, la función no está logrando converger a un punto."
            break
            
    #for e in errors:
      #  print(e)
    
    return {
        "iterations": cont,
        "approximations": approximations,
       # "errors" : errors,
        "divergence": divergence,
        "message": message
    }


def test():
    #function = x**3 + 2*x**2 + 10*x - 20
    #function = sin(x) + x**2/4 - 2
    #function = sin(x) - 2/(1+x**2)
    #function = E**x - x**2
    function = x**2 + 1
    response = newton_main(function, 0)
    print(response)
#test()