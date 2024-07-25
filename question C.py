import numpy as np

def linear_spline(x, x_data, y_data):
  """
  Performs linear spline interpolation.

  Args:
    x: The x-value at which to interpolate.
    x_data: The x-coordinates of the data points.
    y_data: The y-coordinates of the data points.

  Returns:
    The interpolated y-value.
  """
  # Find the interval containing x
  index = np.searchsorted(x_data, x, side='right') - 1
  if index < 0 or index >= len(x_data) - 1:
    raise ValueError("x is outside the data range")

  x1, y1 = x_data[index], y_data[index]
  x2, y2 = x_data[index + 1], y_data[index + 1]
  # Apply the linear spline formula
  y = y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)
  return y
# Given data
x_data = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y_data = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])
# Desired x-value
x = 4.0
# Calculate the interpolated y-value
y_interpolated = linear_spline(x, x_data, y_data)
print("Interpolated y-value at x = 4.0:", y_interpolated)
