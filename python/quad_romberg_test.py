# TEST: Numeric Integration using Trapezoidal and Simpson methods

import numpy as np
from quad import quad_romberg_tab


f = lambda x: np.sin(x)
a = 0.0;
b = np.pi/2
Iexp = -np.cos(b) + np.cos(a)  # Expected integral value

n = 4
R = quad_romberg_tab(a, b, f, n)
print(R)

for i in range(0, n):
    for k in range(0, i+1):
        I = R[i,k]
        E = abs(I-Iexp)/Iexp
        print("I{}{} = {:2e}  |  E={:2e}".format(i, k, I, E))