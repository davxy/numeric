# TEST: Numeric Integration using adaptive Trapezoidal and Simpson methods

from quad import quad_trapezoid, quad_simpson
from quad import quad_trapezoid_adapt, quad_simpson_adapt
import numpy as np
import matplotlib.pyplot as plt


f = lambda x: -2*x**(-3) * np.cos(x**(-2))
a = 0.5;
b = 100;
Iexp = np.sin(10**(-4)) - np.sin(4) # Expected integral value

tol = 10**(-4)  # Error tolerance

print('---------------------------------------')
# Trapezoid adaprive method with relative error
I, x = quad_trapezoid_adapt(a, b, f, tol)
E = abs(Iexp - I)/Iexp      # Relative error
n = len(x)
print('> Trapezoid adaptive method\n I = {}\n E = {}\n n = {}'.format(I, E, n))
# Trapezoid method with relative error
I = quad_trapezoid(a, b, f, n-1)
E = abs(Iexp - I)/Iexp      # Relative error
print('> Trapezoid method\n I = {}\n E = {}\n n = {}'.format(I, E, n))
# Simpson's method with relative error
I = quad_simpson(a, b, f, n-1)
E = abs(Iexp - I)/Iexp      # Relative error
print('> Simpson method\n I = {}\n E = {}\n n = {}'.format(I, E, n))

print('---------------------------------------')
# Trapezoid adaprive method with relative error
I, x = quad_simpson_adapt(a, b, f, tol)
E = abs(Iexp - I)/Iexp      # Relative error
n = len(x)
print('> Simpson adaptive method\n I = {}\n E = {}\n n = {}'.format(I, E, n))
# Trapezoid method with relative error
I = quad_trapezoid(a, b, f, n-1)
E = abs(Iexp - I)/Iexp      # Relative error
print('> Trapezoid method\n I = {}\n E = {}\n n = {}'.format(I, E, n))
# Simpson's method with relative error
I = quad_simpson(a, b, f, n-1)
E = abs(Iexp - I)/Iexp      # Relative error
print('> Simpson method\n I = {}\n E = {}\n n = {}'.format(I, E, n))

# Plot function graph using the last Simpson nodes
N = 10000    # Number of points for a smooth plot
X = np.linspace(a, b, N)
#plt.plot(X, f(X))
fig, ax = plt.subplots()
ax.semilogx(X, f(X))

y = [ f(xi) for xi in x ]
for xi in x:
    ax.semilogx([xi,xi], [0, f(xi)],
             color='black', linestyle='dashed', linewidth=1)
plt.scatter(x, y, linewidths=0.2, marker='+')
plt.grid(True)
plt.show();
