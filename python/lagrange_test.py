# Lagrange interpolating polynomial test

from lagrange import lagrange_eval
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 5])
y = np.square(x)
xx = list(range(0,100,1))
yy = lagrange_eval(xx, x, y)
# Plot the result
plt.scatter(xx, yy, linewidth=0.02)
plt.plot(x, y)
plt.show()
