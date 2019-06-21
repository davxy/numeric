# TEST: Numeric Integration using Trapezoidal and Simpson methods

from quad import quad_trapezoid, quad_simpson
import matplotlib.pyplot as plt
import numpy as np

f = lambda x: 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
a = 0.0;
b = 0.8;
Iexp = 1.640533  # Expected integral value

# n is the number of integration nodes (segments = n-1)
for n in range(2, 11, 2):
    print('-----------------------------------')
    print('n = {}'.format(n))
    # Trapezoid method with relative error
    I = quad_trapezoid(a, b, f, n-1)
    E = abs(I - Iexp) / Iexp
    print("> Trapezoid I = {}, E = {}".format(I, E));
    # Simpson's method with relative error
    I = quad_simpson(a, b, f, n-1)
    E = abs(I - Iexp) / Iexp
    print("> Simpson   I = {}, E = {}".format(I, E));

# Plot using the last approximation number of nodes
N = 1000    # Number of points for a smooth function plot
X = np.linspace(a, b, N)
plt.plot(X, f(X))
X = np.linspace(a, b, n)
for x in X:
    plt.plot([x,x], [0, f(x)],
             color='black', linestyle='dashed', linewidth=1)
plt.plot(X, f(X), color='black', linestyle='dashed', linewidth=1)
plt.grid(True)
plt.show()
