from typing import Callable, Tuple
import matplotlib.pyplot as plt


def secant(function: str, x0: float, x1: float, error: float) -> Tuple[float, float, plt.Figure]:
    """
    Calculates the root of a function using the secant method.

    Parameters:
    function (str): The function to calculate the root of.
    x0 (float): The first initial value.
    x1 (float): The second initial value.
    error (float): The maximum error percentage allowed.

    Returns:
    Tuple[float, float, plt.Figure]: The root, the error percentage, and the graph of the function.
    """
    # Convert the function string to a callable function
    func = eval(f"lambda x: {function}")

    # Initialize variables
    x2 = x1 - ((func(x1) * (x1 - x0)) / (func(x1) - func(x0)))
    error_percent = abs((x2 - x1) / x2) * 100
    iterations = 1
    x_values = [x0, x1, x2]
    y_values = [func(x0), func(x1), func(x2)]

    # Keep iterating until the error is within the allowed range
    while error_percent > error:
        x0 = x1
        x1 = x2
        x2 = x1 - ((func(x1) * (x1 - x0)) / (func(x1) - func(x0)))
        error_percent = abs((x2 - x1) / x2) * 100
        iterations += 1
        x_values.append(x2)
        y_values.append(func(x2))

    # Plot the graph
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.set_title("Secant Method")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Return the root, error percentage, and graph
    return x2, error_percent, fig
