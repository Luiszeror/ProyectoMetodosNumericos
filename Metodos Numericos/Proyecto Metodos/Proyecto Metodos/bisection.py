def bisection(function, x0, x1, error):
    """
    Calculates the root of a function using the bisection method.

    Parameters:
    function (str): The function to calculate the root of.
    x0 (float): The lower bound of the interval.
    x1 (float): The upper bound of the interval.
    error (float): The maximum error percentage allowed.

    Returns:
    tuple: A tuple containing the approximate root, the error percentage, and the graph of the function.
    """
    import matplotlib.pyplot as plt
    import numpy as np

    # Convert the function string to a function that can be evaluated
    func = lambda x: eval(function)

    # Calculate the initial values of f(x0) and f(x1)
    f_x0 = func(x0)
    f_x1 = func(x1)

    # Check if the function has a root in the given interval
    if f_x0 * f_x1 > 0:
        print("La función no tiene una raíz en el intervalo dado.")
        return None

    # Calculate the approximate root
    approx = (x0 + x1) / 2

    # Calculate the error percentage
    error_percent = 100

    # Create a list to store the values of the function for plotting
    x_values = np.linspace(x0, x1, 100)
    y_values = [func(x) for x in x_values]

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, label=function)

    # Iterate until the error is less than the maximum allowed error
    while error_percent > error:
        # Calculate the value of f(approx)
        f_approx = func(approx)

        # Check if the root is between x0 and approx or approx and x1
        if f_x0 * f_approx < 0:
            x1 = approx
            f_x1 = f_approx
        else:
            x0 = approx
            f_x0 = f_approx

        # Calculate the new approximate root
        new_approx = (x0 + x1) / 2

        # Calculate the new error percentage
        error_percent = abs((new_approx - approx) / new_approx) * 100

        # Update the approximate root
        approx = new_approx

        # Add the new point to the plot
        ax.plot(approx, f_approx, 'ro')

    # Add labels and legend to the plot
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Bisección')
    ax.legend()

    # Return the approximate root, error percentage, and plot
    return approx, error_percent, fig
