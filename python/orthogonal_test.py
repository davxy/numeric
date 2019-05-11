# Orthogonal linear system solver tests

import numpy as np
from math import sqrt
from orthogonal import orthogonal

################################################################################

# 2x2 orthogonal matrix
A = np.matrix('1  1;'
              '1 -1', float)
A = A*1.0/sqrt(2.0)
# Known terms vector
b = np.matrix('2; 3')
# Solve the system
x = orthogonal(A, b, 1)
# Check
if np.allclose(b, A*x) == False:
    raise Exception('Orthogonal test failure')

################################################################################

# 2x2 orthogonal matrix
A = np.matrix('2 -2  1;'
              '1  2  2;'
              '2  1 -2', float)
A = A*1.0/3.0
# Known terms vector
b = np.matrix('2; 3; 4')
# Solve the system
x = orthogonal(A, b)
# Check
if np.allclose(b, A*x) == False:
    raise Exception('Orthogonal test failure')