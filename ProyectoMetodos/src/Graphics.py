import matplotlib.pyplot as plt

import numpy as np

from sympy import symbols, lambdify

import json


class Graphics:
    def __init__(self, expr):
        self.expr = expr
        self.x = symbols('x')
        self.f = lambdify(self.x, expr)  # Convertir la expresión a una función evaluable

    # funcion para reducir codigo
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
            x0, x1 = approximations[i - 1], approximations[i]
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
                'x': [approx, approx],
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

    def graph_euler(self, x_vals, y_vals, y_real):
        data = [
            {
                'x': x_vals,
                'y': y_vals,
                'mode': 'lines+markers',
                'name': 'Euler',
                'line': {'color': 'blue'}
            },
            {
                'x': x_vals,
                'y': y_real,
                'mode': 'lines',
                'name': 'Solución Real',
                'line': {'color': 'red', 'dash': 'dot'}
            }
        ]

        layout = {
            'title': 'Método de Euler - Aproximación',
            'xaxis': {'title': 'x'},
            'yaxis': {'title': 'y'},
            'template': 'plotly_white'
        }

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
                'x': [approx, approx],
                'y': [0, self.f(approx)],
                'mode': 'lines',
                'name': f'Aproximación: {approx}',
                'line': {'color': 'red', 'dash': 'dot'}
            })

        # Aproximaciones con líneas tangentes
        for i in range(1, len(approximations)):
            x0, x1 = approximations[i - 1], approximations[i]
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

        x_values = np.linspace(0.01, 150, 1500)  # Empieza desde 0.01 para evitar división por cero y sqrt negativo
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
            x0, x1 = approximations[i - 1], approximations[i]
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

    def graph_trapecio(self, xs, fxs, area):
        x_values = np.linspace(xs[0], xs[-1], 1500)

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

        # Agregar áreas de los trapecios para cada subintervalo
        for i in range(len(xs) - 1):
            x0, x1 = xs[i], xs[i + 1]
            y0, y1 = fxs[i], fxs[i + 1]

            # Agregar el área del trapecio como un relleno
            data.append({
                'x': [x0, x0, x1, x1],
                'y': [0, y0, y1, 0],  # Define los puntos del trapecio
                'fill': 'toself',
                'fillcolor': 'rgba(0, 128, 0, 0.2)',  # Color verde semitransparente
                'line': {'color': 'green', 'dash': 'dash'},
                'name': f'Trapecio {i + 1}'
            })

            # Agregar puntos de evaluación en cada `xi` como marcadores
            data.append({
                'x': [x0],
                'y': [y0],
                'mode': 'markers',
                'marker': {'color': 'red', 'size': 8},
                'name': f'Punto {i}: ({x0:.4f}, {y0:.4f})'
            })

        # Configuración de la gráfica
        layout = {
            'title': 'Gráfica de la función y áreas del método del Trapecio',
            'xaxis': {'title': 'x', 'range': [xs[0] - 1, xs[-1] + 1]},  # Rango ajustado en x
            'yaxis': {'title': 'f(x)', 'range': [min(0, min(fxs)) - 1, max(fxs) + 1]},  # Rango ajustado en y

            # Anotación para mostrar el área calculada en la parte derecha de la gráfica
            'annotations': [
                {
                    'x': xs[-1] + 0.25,  # Colocar la anotación al final del rango en x
                    'y': max(fxs) * 0.9,  # Ubicar ligeramente debajo del valor máximo de fxs
                    'xref': 'x',
                    'yref': 'y',
                    'text': f'Área total ≈ {area:.4f}',
                    'showarrow': False,
                    'font': {'size': 14, 'color': 'black'},
                    'align': 'right'
                }
            ]
        }

        return json.dumps({'data': data, 'layout': layout})

    def graph_simpson(self, xs, fxs, area):
        x_values = np.linspace(xs[0], xs[-1], 1500)
        y_values = self.f(x_values)

        data = [
            {
                'x': x_values.tolist(),
                'y': y_values.tolist(),
                'mode': 'lines',
                'name': 'f(x)',
                'line': {'color': 'blue'}
            }
        ]

        for i in range(0, len(xs) - 1, 2):
            x0, x1, x2 = xs[i], xs[i + 1], xs[i + 2]
            y0, y1, y2 = fxs[i], fxs[i + 1], fxs[i + 2]

            x_parabola = np.linspace(x0, x2, 300)
            y_parabola = (
                    y0 * ((x_parabola - x1) * (x_parabola - x2)) / ((x0 - x1) * (x0 - x2)) +
                    y1 * ((x_parabola - x0) * (x_parabola - x2)) / ((x1 - x0) * (x1 - x2)) +
                    y2 * ((x_parabola - x0) * (x_parabola - x1)) / ((x2 - x0) * (x2 - x1))
            )

            data.append({
                'x': x_parabola.tolist(),
                'y': y_parabola.tolist(),
                'fill': 'toself',
                'fillcolor': 'rgba(255, 165, 0, 0.3)',
                'line': {'color': 'orange'},
                'name': f'Parábola {i // 2 + 1}'
            })

            for j, (x_val, y_val) in enumerate(zip([x0, x1, x2], [y0, y1, y2])):
                data.append({
                    'x': [x_val],
                    'y': [y_val],
                    'mode': 'markers',
                    'marker': {'color': 'red', 'size': 8},
                    'name': f'Punto {i + j}: ({x_val:.4f}, {y_val:.4f})'
                })

            for j in range(i, i + 2):
                x_left = xs[j]
                x_right = xs[j + 1]
                y_left = fxs[j]
                y_right = fxs[j + 1]

                data.append({
                    'x': [x_left, x_left, x_right, x_right],
                    'y': [0, y_left, y_right, 0],
                    'fill': 'toself',
                    'fillcolor': 'rgba(0, 128, 0, 0.3)',
                    'line': {'color': 'green'},
                    'name': f'Rectángulo/Trapecio {i // 2 + 1}'
                })

        layout = {
            'title': 'Gráfica de la función y áreas del método de Simpson',
            'xaxis': {'title': 'x', 'range': [xs[0] - 1, xs[-1] + 1]},
            'yaxis': {'title': 'f(x)', 'range': [min(0, min(fxs)) - 1, max(fxs) + 1]},

            'annotations': [
                {
                    'x': xs[-1] + 0.25,
                    'y': max(fxs) * 0.9,
                    'xref': 'x',
                    'yref': 'y',
                    'text': f'Área total ≈ {area:.4f}',
                    'showarrow': False,
                    'font': {'size': 14, 'color': 'black'},
                    'align': 'right'
                }
            ]
        }

        # Retornar los datos y la configuración en formato JSON para Plotly
        return json.dumps({'data': data, 'layout': layout})


