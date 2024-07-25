def trapezoidal_integration(f, a, b, n):
    """Calculates the integral using the trapezoidal method.

    Args:
        f: The function to integrate.
        a: The lower limit of integration.
        b: The upper limit of integration.
        n: The number of subintervals.

    Returns:
        The approximate integral.
    """
    dx = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return dx * (np.sum(y) - (y[0] + y[-1]) / 2)
