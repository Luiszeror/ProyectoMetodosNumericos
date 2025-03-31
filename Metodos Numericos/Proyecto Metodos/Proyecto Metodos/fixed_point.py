def fixed_point(function, initial_value, error):
    import matplotlib.pyplot as plt
    import numpy as np

    # Define the function to be evaluated
    def f(x):
        return eval(function)

    # Define the fixed point iteration function
    def g(x):
        return eval(function.replace("x", str(x)))

    # Initialize variables
    x0 = initial_value
    x1 = g(x0)
    error_percent = 100

    # Create lists to store values for plotting
    x_values = [x0, x1]
    y_values = [f(x0), f(x1)]

    # Iterate until desired error is achieved
    while error_percent > error:
        x0 = x1
        x1 = g(x0)
        error_percent = abs((x1 - x0) / x1) * 100

        # Append values for plotting
        x_values.append(x1)
        y_values.append(f(x1))

    # Create plot
    x = np.linspace(min(x_values), max(x_values), 100)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, label="f(x)")
    ax.plot(x, x, label="y=x")
    ax.plot(x_values, y_values, 'o-', label="Fixed Point Iteration")
    ax.legend()
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Fixed Point Iteration")

    # Return root, error percent, and plot
    return x1, error_percent, fig
