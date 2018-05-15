# PA=LU factorization algorithm

import numpy as np
from triangular import triangular


def palu_factor(A):
    '''
    input:
        - A: a numpy coefficient square matrix
    output:
        A tuple consisting of two elements
        - A: LU factorized matrix with the upper trianguar part
             containing U and the lower trianguar part (diagonal
             excluded) containing L.
        - p: permutation vector
    '''
    # Get the matrix size
    n = A.shape[0]
    p = list(range(0, n))
    if n != A.shape[1]:
        raise Exception('The coefficient matrix should be square')
    for i in range(0,n-1):
        # Get the max row number
        maxrow = abs(A[i:n,i]).argmax()
        # align vector row with matrix row
        maxrow = maxrow + i
        maxval = A[maxrow,i]
        if maxval == 0:
            raise Exception('The matrix is not LU factorizable')
        if maxrow > i:
            # rows swap
            A[[i,maxrow]]=A[[maxrow,i]]
            #p[[i,maxrow]]=p[[maxrow,i]]
            p[i], p[maxrow] = p[maxrow], p[i]
        # computation of the i-th Gauss vector that will be
        # part of the L matrix
        A[i+1:,i] = A[i+1:,i]/A[i,i]
        # recomputation of the square sub-matrix defined under
        # the i-th row and after the i-th column
        A[i+1:,i+1:] = A[i+1:,i+1:] - A[i+1:,i]*A[i,i+1:]
    return (A,p)


if __name__ == '__main__':
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
