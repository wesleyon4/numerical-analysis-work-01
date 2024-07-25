def spline_interpolation(x, y, kind='cubic'):
  """Performs spline interpolation.

  Args:
      x: The x-coordinates of the data points.
      y: The y-coordinates of the data points.
      kind: The type of spline (default: 'cubic').

  Returns:
      The interpolation function.
  """
  f = interp1d(x, y, kind=kind)
  return f
