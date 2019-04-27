'''
Numerical differentiation error test.

Finite Forward Difference (FFD) and Symmetric Differential Quotient (SDQ)
errors magnitude are compared for a known function on a fixed point x0.

The test also shows that, after a certain threshold, both the methods are 
heavily affected by numerical cancellation.

Note that the SDQ method produces smaller errors.
'''

import numpy as np
import matplotlib.pyplot as plt

a = 0.5
ddx = np.cos(a)
# Get 100 numbers between 10^-17 and 10^0 evenly spaced on a log scale.
hh = np.logspace(-17, 0, 100, endpoint=True)
ffd = []
sdq = []
ffd_err = []
sdq_err = []
for h in hh:
    val = (np.sin(a+h)-np.sin(a))/h
    ffd.append(val)
    ffd_err.append(abs(ddx - val))
    val = (np.sin(a+h)-np.sin(a-h))/(2*h)
    sdq.append(val)
    sdq_err.append(abs(ddx - val))
# Print a tabular form of the results
print('ddx = {}'.format(ddx))
print('h\tFFD\tErr\tSDQ\tErr')
for h,a,b,c,d in zip(hh,ffd, ffd_err, sdq, sdq_err):
    print('{:.9f} {:.9f} {:.9f} {:.9f} {:.9f}'.format(h,a,b,c,d))
# Plot the graph
plt.loglog(hh, ffd_err)
plt.loglog(hh, sdq_err)
plt.grid(True)
plt.xlabel('h')
plt.ylabel('error')
plt.legend(['ffd','sdq'])
plt.show()
