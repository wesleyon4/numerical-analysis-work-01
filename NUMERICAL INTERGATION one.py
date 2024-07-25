def rectangular_integration(f, a, b, n):
    """Calculates the integral using the rectangular method.
    Args:
        f: The function to integrate.
        a: The lower limit of integration.
        b: The upper limit of integration.
        n: The number of subintervals.

    Returns:
        The approximate integral.
    """
    dx = (b - a) / n
    x = np.linspace(a, b, n + 1)[:-1]
    return dx * np.sum(f(x))
