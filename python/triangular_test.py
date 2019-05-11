# Triangular linear system solver test

import numpy as np
from triangular import triangular

################################################################################

# Lower triangular matrix
A = np.matrix('12  0  0  0  0;'
              '18 38  0  0  0;'
              '51  4 57  0  0;'
              '53  3  8  2  0;'
              '31 26 4 16  60', float)
# Known terms vector
b = np.matrix('68; 9; 46; 43; 35')
# Solve the system
x = triangular(A, b, 1)
# Check
if np.allclose(b, A*x) == False:
    raise Exception('Lower triangular test failure')

################################################################################

# Upper triangular matrix
A = np.matrix('12 48  2 51 49;'
              ' 0 38 32 51  5;'
              ' 0  0 57  2 31;'
              ' 0  0  0  2 53;'
              ' 0  0  0  0 60', float)
# Known terms vector
b = np.matrix('7; 31; 32; 34; 22')
# Solve the system
x = triangular(A, b, 0)
# Check
if np.allclose(b, A*x) == False:
    raise Exception('Upper triangular test failure')
