import numpy as np

def trapezoidal_rule(f, a, b, n):
  """
  Approximates the definite integral of a function using the trapezoidal rule.

  Args:
    f: The function to integrate.
    a: The lower limit of integration.
    b: The upper limit of integration.
    n: The number of subintervals.

  Returns:
    The approximate integral.
  """

  h = (b - a) / n  # Width of each subinterval
  x = np.linspace(a, b, n + 1)  # Equally spaced points
  y = f(x)

  # Apply the trapezoidal rule formula
  integral = h * (y[0] + y[-1] + 2 * np.sum(y[1:-1])) / 2

  return integral
