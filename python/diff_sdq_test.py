# Given an ordered set of randomly distributed nodes and the y-axis value
# relative to each node (e.g. the result of a non-periodic sampling) we want
# to estimate the derivative at each of the sampling points using the FFD
# method.
#
# In this experiment, the SDQ method is not an option since the nodes are not
# equally spaced.
#
# The resulting graph clearly shows that, before a certain threshold is reached,
# the error diminishes regularly as the value of h gets smaller. From the
# threshold point (~ 10^-5 for the SDQ and ~ 10^-8 for the FFD), as h gets even
# smaller, the error starts to grow in a fuzzy way because of cancellation.
#
# Also note that, even though cancellation issues starts to manifest earlier
# in the SDQ method, the error becomes smaller earlier as well: for h~10^-5,
# the SDQ error ~10^12  while the FFD error is ~10^-6.
#
# The empirical results are compatible with the theoretical ones.

import numpy as np
import matplotlib.pyplot as plt

N = 20
x = np.linspace(-np.pi, np.pi, N)
#fx = np.sin(x)
#dx = np.cos(x)
fx = x**6 - 2*x**5 + x**3 - x**2 + 3*x + 1
dx = 6*x**5 - 10*x**4 + 3*x**2 - 2*x + 3
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
