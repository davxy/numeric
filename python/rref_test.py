# Reduced row echelon form algorithm test

import numpy as np
from rref import rref


# Test if the reduced row echelon function
A = np.matrix(' 1  2  -1;'
              ' 2  3  -1;'
              '-2, 0, -3',
              float);
b = np.matrix('-4; -11; 22')

################################################################################
# Find the inverse first

# Augmented matrix
M = np.column_stack((A,np.identity(3)))
# Transform in row echelon form
R = rref(M)
# Extract the inverse
A1 = R[:,3:6]
# Test inverse
if np.allclose(np.identity(3), A*A1) == False:
    raise Exception('Inverse find failure')
# Test
x = A1*b
if np.allclose(b, A*x) == False:
    raise Exception('System resolution test failure')

################################################################################
# Direct resolution

# Augmented matrix
M = np.column_stack((A,b))
# Transform in row echelon form
R = rref(M)
# Check the result
x = R[:,3]
# Check
if np.allclose(b, A*x) == False:
    raise Exception('System resolution test failure')