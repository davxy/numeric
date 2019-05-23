# Newton interpolating polynomial test

import numpy as np
from newton_interp import newton_interp
import matplotlib.pyplot as plt

x = np.array([15, 42, 30])
y = np.square(x)
X = np.linspace(0, 100, 100)
Y = newton_interp(x, y, X)

# Plot the result
plt.scatter(x, y)
plt.plot(X, Y)
plt.show()
