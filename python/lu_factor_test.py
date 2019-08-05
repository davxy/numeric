# LU factorization algorithm test

from lu_factor import lu_factor
import numpy as np
from triangular import triangular


# TEST: LU factorization
# Non singular 6x6 matrix
A = np.matrix('29 11 59  9 13;'
              '41 27  3 13  1;'
              '53 62 23 13 50;'
              '61 61 54 40 29;'
              '49 27  0 18 62', float)
print('A = \n', A)
# LU factorization (deep-copy of A because we need it or the "check")
B = lu_factor(np.matrix(A))
print('B = \n', B)
# Extract lower part
L = np.matrix(np.tril(B,-1) + np.identity(5))
print('L = \n', L)
# Extract upper part
U = np.matrix(np.triu(B))
print('U = \n', U)
# Check
if np.allclose(A, L*U) == False:
    raise Exception('LU factorizzation test failure')

# TEST: System Resolution
# Ax = LUx = b
b = np.matrix('68; 9; 45; 43; 35')
# Lk = b
k = triangular(L, b, 1)
# Ux = k
x = triangular(U, k, 0)
# Check
if np.allclose(b, A*x) == False:
    raise Exception('System resolution test failure')

