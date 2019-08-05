# Lagrange interpolating polynomial test

from lagrange import lagrange
import matplotlib.pyplot as plt
import numpy as np


# Three points are sufficient to interpolate a polynomial of degree 2
x = np.array([15, 42, 30])
y = np.square(x)
X = np.linspace(0, 100, 100)
Y = lagrange(x, y, X)

# Plot the result
plt.scatter(x, y)
plt.plot(X, Y)
plt.show()
