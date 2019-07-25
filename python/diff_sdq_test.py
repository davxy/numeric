# Given an ordered set of uniformly distributed nodes and the y-axis value
# relative to each node (e.g. the result of a periodic sampling) we want
# to estimate the derivative at each of the sampling points using the SDQ
# method.

import matplotlib.pyplot as plt
import numpy as np


N = 20
x = np.linspace(-np.pi, np.pi, N)
fx = np.sin(x)
dx = np.cos(x)
#fx = x**6 - 2*x**5 + x**3 - x**2 + 3*x + 1
#dx = 6*x**5 - 10*x**4 + 3*x**2 - 2*x + 3
h = x[1] - x[0]
print("h = ", h);

sdq = np.zeros(N)
sdq[0]   = (fx[1] - fx[0]) / h
sdq[N-1] = (fx[N-1] - fx[N-2]) / h
for i in range(1, N-1):
    sdq[i] = (fx[i+1] - fx[i-1]) / (2*h)

err = abs(dx - sdq)

print('| Dx           | SDQ          | Err')
for a,b,c in zip(dx, sdq, err):
    print('| {:.9f} | {:.9f} | {:.9f}'.format(a, b, c))

plt.text(2.2, 0.6, 'N = {}'.format(N))
plt.plot(x, dx)
plt.plot(x, sdq)
plt.legend(['dx','sdq'])
plt.show()
