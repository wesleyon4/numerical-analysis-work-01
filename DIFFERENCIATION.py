def finite_difference(f, x, h=1e-6):
    """Calculates the numerical derivative using the central difference method.
finite differenciation
    Args:
        f: The function to differentiate.
        x: The point at which to evaluate the derivative.
        h: The step size (default: 1e-6).

    Returns:
        The approximate derivative at x.
    """
    return (f(x + h) - f(x - h)) / (2 * h)
