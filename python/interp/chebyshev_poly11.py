import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.chebyshev import Chebyshev, cheb2poly
import math

# Get the polynomial
deg = 11
c = Chebyshev(list(np.zeros(deg, int)) + [1])

# Plot the Chebyshev polynomial
xx = np.linspace(-1, 1, 100)
yy = [ c(x) for x in xx ]
plt.plot(xx, yy)

xi = [ math.cos((2*x+1)*math.pi/(2*deg)) for x in range(0, deg) ]
plt.plot(xi,list(np.zeros(len(xi))),'o')

plt.plot(xx, [ math.sqrt(1-x**2) for x in xx ],
         color='black', linestyle='dashed', linewidth=1)
for x in xi:
    plt.plot([x,x],[0,math.sqrt(1-x**2)],
             color='black', linestyle='dashed', linewidth=1)

plt.grid(True)
plt.show()

