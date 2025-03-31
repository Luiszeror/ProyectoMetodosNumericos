import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols
from sympy import lambdify
from sympy import sympify

print("")
x=symbols("x")
fn=sympify((2*x**3)-(9*x**2)+6)
f=lambdify(x,fn)

#Iniciar variables

a=float(input("Valor de a: "))
b=float(input("Valor de b: "))
crit = float(input(" Criterio de paro: "))
i=0 #Iniciar el contador
ea=1 #Iniciar la variable de error
x_anterior = 0 #Iniciar la variable de x anterior

#Criterio inicial para verificar si la solución está en el intervalo seleccionado

if f(a)*f(b)<0:

   print("")
   print("i","a","b","xr","ea(%)")

   while ea>crit:
       xr= (a+b)/2
       ea=abs((xr-x_anterior)/xr)  #Calcular el error absoluto

       if f(xr)*f(a)<0:
           b=xr
       else:
           a=xr

       x_anterior=xr

       print(i,a,b,xr,round(ea*100,9))
       i=i+1  #Aumentar el contador

   print(" ")
   print("El valor de x es: {}, con un error de: {}%".format(round(xr,9),round(ea*100,9)))


else:  #f(a)*f(b)>=0

   #Si no hay raiz o se seleccionan 2 en un intervalo
   print("")
   print("La función no tiene raiz en el intervalo de "+"x="+str(a)+"ax="+str(b))
   print("Ingresar otros valores iniciales")