from typing import Callable, Tuple
import matplotlib.pyplot as plt


def trapezoidal(
    function: str, lower_limit: float, upper_limit: float, intervals: int
) -> Tuple[float, float, plt.Figure]:
    """
    Calculates the approximate definite integral of a function using the trapezoidal rule.

    Args:
    - function (str): The function to integrate.
    - lower_limit (float): The lower limit of integration.
    - upper_limit (float): The upper limit of integration.
    - intervals (int): The number of intervals to use in the approximation.

    Returns:
    - A tuple containing:
        - The approximate value of the definite integral.
        - The percent error of the approximation.
        - The graph of the function and the trapezoids used in the approximation.
    """
    try:
        f = lambda x: eval(function)
        h = (upper_limit - lower_limit) / intervals
        x_values = [lower_limit + i * h for i in range(intervals + 1)]
        y_values = [f(x) for x in x_values]
        approx = h * (y_values[0] + y_values[-1] + 2 * sum(y_values[1:-1])) / 2
        actual = integrate.quad(f, lower_limit, upper_limit)[0]
        error_percent = abs((actual - approx) / actual) * 100
        fig, ax = plt.subplots()
        ax.plot(x_values, y_values, "b")
        ax.fill_between(x_values, y_values, 0, where=[True] * (intervals + 1), alpha=0.2)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Trapezoidal Rule Approximation")
        return approx, error_percent, fig
    except:
        print("Error: Por favor ingrese los datos correctamente.")
        return None, None, None
