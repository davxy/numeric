# LU factorization algorithm

import numpy as np
from triangular import triangular

def lu_factor(A):
    '''
    input:
        - A: a numpy coefficient square matrix
    output:
        - A: LU factorized matrix with the upper trianguar part
             containing U and the lower trianguar part (diagonal
             excluded) containing L.
    '''
    # Get the matrix size
    n = A.shape[0]
    if n != A.shape[1]:
        print('The coefficient matrix should be square')
        return None
    for i in range(0,n-1):
        if A[i,i] == 0:
            print('The matrix is not LU factorizable')
            return
        # computation of the i-th Gauss vector that will be
        # part of the L matrix
        A[i+1:,i] = A[i+1:,i]/A[i,i]
        # recomputation of the square sub-matrix defined under
        # the i-th row and after the i-th column
        A[i+1:,i+1:] = A[i+1:,i+1:] - A[i+1:,i]*A[i,i+1:]
    return A


# Simple self test
if __name__ == "__main__":
    # TEST: LU factorization
    # Non singular 6x6 matrix
    A = np.matrix('29 11 59  9 13;'
                  '41 27  3 13  1;'
                  '53 62 23 13 50;'
                  '61 61 54 40 29;'
                  '49 27  0 18 62', float)
    print('A = ', A)
    # LU factorization (deep-copy of A because we need it later)
    B = lu_factor(np.matrix(A))
    print('B = ', B)
    # Extract lower part
    L = np.matrix(np.tril(B,-1) + np.identity(5))
    print('L = ', L)
    # Extract upper part
    U = np.matrix(np.triu(B))
    print('U = ', U)
    # Check
    LU = L*U
    print('LU = ', LU)
    if np.allclose(A, LU) == False:
        print('LU factorizzation test failure')

    # TEST: System Resolution
    # Ax = LUx = b 
    b = np.matrix('68; 9; 45; 43; 35')
    # Lk = b
    k = triangular(L, b, 1)
    # Ux = k
    x = triangular(U, k, 0)
    # Check
    if np.allclose(b, A*x) == False:
        print('System resolution test failure')
    