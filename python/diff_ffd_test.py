# Given an ordered set of randomly distributed nodes and the y-axis value
# relative to each node (e.g. the result of a non-periodic sampling) we want
# to estimate the derivative at each of the sampling points using the FFD
# method.
#
# In this experiment, the SDQ method is not an option since the nodes are not
# equally spaced.

import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.uniform(-np.pi, np.pi, N)
#x = np.linspace(-np.pi, np.pi, N)
x = np.sort(x)
x[0] = -np.pi
x[N-1] = np.pi
fx = np.sin(x)
dx = np.cos(x)
#fx = x**6 - 2*x**5 + x**3 - x**2 + 3*x + 1
#dx = 6*x**5 - 10*x**4 + 3*x**2 - 2*x + 3

ffd = np.diff(fx)/np.diff(x)
ffd = np.concatenate((ffd,[ffd[len(ffd)-1]]))

err = abs(dx - ffd)

print('| Dx           | FFD          | Err')
for a,b,c in zip(dx, ffd, err):
    print('| {:.9f} | {:.9f} | {:.9f}'.format(a, b, c))

plt.text(2.2, 0.6, 'N = {}'.format(N))
plt.plot(x, dx)
plt.plot(x, ffd)
plt.legend(['dx','ffd'])
plt.show()
