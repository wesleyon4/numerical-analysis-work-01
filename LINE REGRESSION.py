def linear_regression(X, y):
  """Performs linear regression.
  Args:
      X: The independent variables.
      y: The dependent variable.
  Returns:
      The estimated coefficients and other statistics.
  """
  X = sm.add_constant(X)  # Add constant term
  model = sm.OLS(y, X).fit()
  return model.summary()