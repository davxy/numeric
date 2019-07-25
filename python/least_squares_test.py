# Least squares interpolation test

from math import sin
from random import uniform

from least_squares import least_squares
import matplotlib.pyplot as plt
import numpy as np


# Interpolation interval
xmin = -2*np.pi
xmax =  2*np.pi
# Function
f = lambda x: sin(x)
# f = lambda x: 4*x
# Number of samples
s = 50
# Interpolating polynomial degree
d = 4

# Sample points
x = np.linspace(xmin, xmax, s)
y = np.asarray([f(xi) + uniform(-0.7, 0.7) for xi in x ])
# Query points
X = np.linspace(xmin, xmax, 100)
# Evaluation
Y = least_squares(x, y, d, X)

# Plot results
# Plot the result
plt.scatter(x, y, linewidths=0.2, marker='o', color='orange')
plt.plot(X, Y, linewidth=1)
plt.legend(['deg={}'.format(d)])
plt.show()

