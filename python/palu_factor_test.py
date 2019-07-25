# PA=LU factorization algorithm test

import numpy as np
from palu_factor import palu_factor
from triangular import triangular


np.set_printoptions(suppress=True, precision=5)
# TEST: PA=LU factorization

# Coefficient matrix
A = np.matrix(' 0 41 53 12 62 26;'
              '43 49 61 60 22 27;'
              '65 25 56 38 43 43;'
              '37  0 24 42 26 56;'
              '26 28 41 15 42 24;'
              '13 50 48 36 46 28 ', float)
print('A = \n', A)
# LU factorization (deep-copy of A because we need it or the "check")
B, p = palu_factor(np.matrix(A))
print('B = \n', B)
# Extract lower part
L = np.matrix(np.tril(B,-1) + np.identity(6))
print('L = \n', L)
# Extract upper part
U = np.matrix(np.triu(B))
print('U = \n', U)
# Check
if np.allclose(A[p], L*U) == False:
    raise Exception('LU factorization test failure')

# TEST: System Resolution
# Ax = b => PAx = Pb => LUx = Pb
# LUx = Pb
b = np.matrix('33; 35; 2; 49; 53; 21')
# Lk = Pb (note the permutation of b using the index vector p)
k = triangular(L, b[p], 1)
# Ux = k
x = triangular(U, k, 0)
# Check
if np.allclose(b, A*x) == False:
    raise Exception('System Resolution test failure')
