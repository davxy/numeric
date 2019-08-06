import numpy as np
from chol_factor import chol_factor
from triangular import triangular

# TEST: Cholesky factorization (LL')

# Symmetric positive definite matrix
A = np.matrix('5    1.2  0.3 -0.6;'
              '1.2  6   -0.4  0.9;'
              '0.3 -0.4  8    1.7;'
             '-0.6  0.9  1.7  10');
# Computation of the L factor
L = chol_factor(A)
# Check
if np.allclose(A, np.dot(L, L.transpose())) == False:
    raise Exception('QR factorizzation test failure')


# TEST: System Resolution

# Ax = LL'x = b
b = [ 68, 9, 45, 35 ]
# Lk = b
k = triangular(L, b, 1)
# L'x = k
x = triangular(L.transpose(), k, 0)
# Check
b1 = np.dot(A, x)
if np.allclose(b, b1.flatten()) == False:
    raise Exception('System resolution failure')
