def polynomial_fitting(x, y, degree):
    """Fits a polynomial to the data points.

    Args:
        x: The x-coordinates of the data points.
        y: The y-coordinates of the data points.
        degree: The degree of the polynomial.
    Returns:
        The polynomial coefficients.
    """
    p = np.polyfit(x, y, degree)
    return p
