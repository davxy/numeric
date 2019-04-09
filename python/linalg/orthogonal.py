# Orthogonal system test

import numpy as np
from math import sqrt

def orthogonal(A, b, chk=0):
    # Optionally chk for orthogonality
    if chk == 1 and is_orthogonal(A) == 0:
        raise Exception('Not orthogonal input matrix')
    return A.transpose()*b

def is_orthogonal(A):
    return np.allclose(A*A.transpose(), np.identity(len(b)))


if __name__ == "__main__":
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
