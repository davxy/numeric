import numpy as np
from chol_factor import chol_factor
from triangular import triangular

# TEST: Cholesky factorization (LL')

# Symmetric positive definite matrix
A = np.matrix('5    1.2  0.3 -0.6;'
              '1.2  6   -0.4  0.9;'
              '0.3 -0.4  8    1.7;'
             '-0.6  0.9  1.7  10');
print('A = \n', A)
# Computation of the L factor
L = chol_factor(A)
print('L = \n', L)
# Check
if np.allclose(A, np.dot(L, L.transpose())) == False:
    raise Exception('QR factorizzation test failure')


# TEST: System Resolution

# Ax = LL'x = b
b = np.matrix("68; 9; 45; 35")
print('b = \n', b)
# Lk = b
k = triangular(L, b, 1)
print('k = \n', k)
# L'x = k
x = triangular(L.transpose(), k, 0)
print('x = \n', x)
# Check
b1 = np.dot(A, x)
print('b1 = \n', b1)
if np.allclose(b, b1) == False:
    raise Exception('System resolution failure')
