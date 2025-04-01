import matplotlib.pyplot as plt

import numpy as np

from sympy import symbols, lambdify

import json

class Graphics:
    def __init__(self, expr):
        self.expr = expr
        self.x = symbols('x')
        self.f = lambdify(self.x, expr) # Convertir la expresión a una función evaluable

    #funcion para reducir codigo
    def basic_config(self, approximations, x_values, y_values):
        
        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, label='f(x)', color='blue')
        plt.axhline(0, color='black', lw=0.5, ls='--')  # Línea horizontal en y=0
        plt.axvline(0, color='black', lw=0.5, ls='--')  # Línea vertical en x=0

        # Graficar las aproximaciones
        for approx in approximations:
            plt.plot(approx, self.f(approx), 'ro')  # Puntos rojos en las aproximaciones

        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid()

    def graph_punto_fijo(self, approximations, xo):
    # Asegurar que xo esté en las aproximaciones
        if approximations[0] != xo:
            approximations.insert(0, xo)

        # Generar puntos para graficar la función
        x_values = np.linspace(-20, 20, 400)
        y_values = self.f(x_values)

        # Estructura de datos para Plotly
        data = [
            {
                'x': x_values.tolist(),
                'y': y_values.tolist(),
                'mode': 'lines',
                'name': 'f(x)',
                'line': {'color': 'blue'}
            }
        ]

        # Agregar las aproximaciones como puntos y líneas
        for i in range(1, len(approximations)):
            x0, x1 = approximations[i-1], approximations[i]
            y0 = self.f(x0)

            # Línea entre (x0, f(x0)) y (x1, 0)
            data.append({
                'x': [x0, x1],
                'y': [y0, 0],
                'mode': 'lines',
                'name': f'Iteración {i}',
                'line': {'color': 'purple', 'dash': 'dash'}
            })

        # Puntos de aproximación
        for approx in approximations:
            data.append({
                'x':[approx, approx],
                'y': [0, self.f(approx)],
                'mode': 'lines',
                'name': f'Aproximación: {approx}',
                'line': {'color': 'red', 'dash': 'dot'}
            })

        # Configuración de la gráfica
        layout = {
            'title': 'Método de Punto Fijo - Gráfica de Aproximaciones',
            'xaxis': {'title': 'x', 'range': [-20, 20]},
            'yaxis': {'title': 'f(x)', 'range': [-20, 20]},
            'template': 'plotly_white'
        }

        # Retornar los datos y la configuración en formato JSON
        return json.dumps({'data': data, 'layout': layout})
    

   
     # Método de Newton con líneas tangentes
    
    def graph_newton(self, approximations, xo):
        # Asegurar que xo esté en las aproximaciones
        if approximations[0] != xo:
            approximations.insert(0, xo)

        # Generar puntos para graficar la función
        x_values = np.linspace(-20, 20, 400)
        y_values = self.f(x_values)

        # Estructura de datos para Plotly
        data = [
            {
                'x': x_values.tolist(),
                'y': y_values.tolist(),
                'mode': 'lines',
                'name': 'f(x)',
                'line': {'color': 'blue'}
            }
        ]

        # Punto inicial
        for approx in approximations:
            data.append({
                'x':[approx, approx],
                'y': [0, self.f(approx)],
                'mode': 'lines',
                'name': f'Aproximación: {approx}',
                'line': {'color': 'red', 'dash': 'dot'}
            })

        # Aproximaciones con líneas tangentes
        for i in range(1, len(approximations)):
            x0, x1 = approximations[i-1], approximations[i]
            y0 = self.f(x0)

            # Línea tangente entre (x0, f(x0)) y (x1, 0)
            data.append({
                'x': [x0, x1],
                'y': [y0, 0],
                'mode': 'lines',
                'name': f'Iteración {i}',
                'line': {'color': 'purple', 'dash': 'dash'}
            })

        # Puntos de aproximación
        data.append({
            'x': approximations,
            'y': [self.f(x) for x in approximations],
            'mode': 'markers',
            'marker': {'color': 'red', 'size': 8},
            'name': 'Aproximaciones'
        })

        # Configuración de la gráfica
        layout = {
            'title': 'Método de Newton - Gráfica de Aproximaciones',
            'xaxis': {'title': 'x', 'range': [-20, 20]},
            'yaxis': {'title': 'f(x)', 'range': [min(y_values) - 1, max(y_values) + 1]},
            'template': 'plotly_white'
        }

        # Retornar los datos y la configuración en formato JSON
        return json.dumps({'data': data, 'layout': layout})
    
    def graph_biseccion(self, xi, xu, approximations):
        print("expresion", self)
        print(f"xi: {xi}, xu: {xu}, approximations: {approximations}") 

        x_values = np.linspace(-150, 150, 1500)  
        y_values = self.f(x_values)

        # Estructura de datos para Plotly
        data = [
            {
                'x': x_values.tolist(),
                'y': y_values.tolist(),
                'mode': 'lines',
                'name': 'f(x)',
                'line': {'color': 'blue'}
            }
        ]

        # Agregar aproximaciones
        for approx in approximations:
            data.append({
                'x': [approx, approx],
                'y': [0, self.f(approx)],
                'mode': 'lines',
                'name': f'Aproximación: {approx}',
                'line': {'color': 'red', 'dash': 'dot'}
            })

        # Configuración de la gráfica
        layout = {
            'title': 'Gráfica de la función y aproximaciones del método de Bisección',
            'xaxis': {'title': 'x', 'range': [-20, 20]},  # Rango fijo en x
            'yaxis': {'title': 'f(x)', 'range': [-20, 20]},  # Rango fijo en y
        }

        # Retornar los datos y la configuración en formato JSON
        return json.dumps({'data': data, 'layout': layout})

    def graph_secante(self, approximations):
        print(f"approximations: {approximations}")

        x_values = np.linspace(-150, 150, 1500)  
        y_values = self.f(x_values)
        
        # Estructura de datos para Plotly
        data = [
            {
                'x': x_values.tolist(),
                'y': y_values.tolist(),
                'mode': 'lines',
                'name': 'f(x)',
                'line': {'color': 'blue'}
            }
        ]

        for i in range(1, len(approximations)):
            x0, x1 = approximations[i-1], approximations[i]
            y0, y1 = self.f(x0), self.f(x1)

            data.append({
                'x': [x0, x1],
                'y': [y0, y1],
                'mode': 'lines',
                'name': f'Secante {i}',
                'line': {'color': 'green', 'dash': 'dash'}
            })

            
            data.append({
                'x': [x0],
                'y': [y0],
                'mode': 'markers',
                'marker': {'color': 'red', 'size': 8},
                'name': f'Aproximación {i}: {x0:.4f}'
            })
            
            
            data.append({
                'x': [x0, x0],
                'y': [0, y0], 
                'mode': 'lines',
                'line': {'color': 'red', 'dash': 'dot'},
                'name': f'Línea a f({x0:.4f})'
            })

       
        layout = {
            'title': 'Gráfica de la función y aproximaciones del método de la Secante',
            'xaxis': {'title': 'x', 'range': [-20, 20]},  
            'yaxis': {'title': 'f(x)', 'range': [-20, 20]}, 
        }
        

        return json.dumps({'data': data, 'layout': layout})
    