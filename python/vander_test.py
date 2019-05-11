# Plot the Vandermonde matrix condition number given an increasing
# matrix order

import numpy as np
import matplotlib.pyplot as plt

ordermax = 20
vcond = []
axis  = list(range(1, ordermax+1)) 
for n in axis:
    x = np.empty(n+1)
    for i in range(0, n+1):
        x[i] = float(i)/n
    V = np.vander(x);
    vcond.append(np.linalg.cond(V))
plt.ylabel('log(cond)')
plt.xlabel('order')
plt.semilogy(axis, vcond)
plt.grid(True)
plt.show()
