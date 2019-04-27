'''
Given an ordered set of randomly distributed nodes and the y-axis value
relative to each node (e.g. the result of a non-periodic sampling) we want
to estimate the derivative at each of the sampling points using the FFD
method.

In this experiment, the SDQ method is not an option since the nodes are not
equally spaced.

The resulting graph clearly shows that, before a certain threshold is reached,
the error diminishes regularly as the value of h gets smaller. From the
threshold point (~ 10^-5 for the SDQ and ~ 10^-8 for the FFD), as h gets even
smaller, the error starts to grow in a fuzzy way because of cancellation.

Also note that, even though cancellation issues starts to manifest earlier
in the SDQ method, the error becomes smaller earlier as well: for h~10^-5,
the SDQ error ~10^12  while the FFD error is ~10^-6.

The empirical results are compatible with the theoretical ones.
'''

import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.uniform(-np.pi, np.pi, N)
x = np.sort(x)
fx = np.sin(x)
dx = np.cos(x)

ffd = np.diff(fx)/np.diff(x)
ffd = np.concatenate((ffd,[ffd[len(ffd)-1]]))

err = abs(dx - ffd)

print('Dx\tFFD\tErr')
for a,b,c in zip(dx, ffd, err):
    print('{:.9f}\t{:.9f}\t{:.9f}'.format(a, b, c))

plt.text(2.2, 0.6, 'N = {}'.format(N))
plt.plot(x, dx)
plt.plot(x, ffd)
plt.legend(['dx','ffd'])
plt.show()
