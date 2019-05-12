# Lagrange interpolating polynomial test

from lagrange import lagrange_eval
import numpy as np
import matplotlib.pyplot as plt

# Three points are sufficient to interpolate a polynomial of degree 2
x = np.array([15, 42, 30])
y = np.square(x)
X = list(range(0,100,1))
Y = lagrange_eval(X, x, y)

# Plot the result
plt.scatter(x, y)
plt.plot(X, Y)
plt.show()
