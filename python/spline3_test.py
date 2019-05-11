# Cubic spline interpolation test

from spline3 import spline3
import numpy as np
import matplotlib.pyplot as plt

nq = 100    # query points
n  = 15     # interpolation nodes

x = np.linspace(-1, 1, n)
y = np.array([ 1.0 / (1 + 25*x[i]**2) for i in range(0, n) ])

# nq evenly spaced values between min(x) and max(x)
X = np.linspace(min(x), max(x), nq)
# Get true function values at the query points
f = [ 1.0 / (1 + 25*X[i]**2) for i in range(0, nq) ]

# Get Y values at query points using cubic spline interpolation
Y = spline3(x, y, X)

# Plot the result
plt.scatter(X, Y, linewidths=0.2, marker='+')
plt.plot(X, f)
plt.scatter(x, y, linewidths=0.2, marker='o')
plt.show()
