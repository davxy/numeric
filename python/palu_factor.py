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
    p = np.empty([n,1])
    if n != A.shape[1]:
        print('The coefficient matrix should be square')
        return (A,p)
    for i in range(0,n-1):
        maxrow = max(abs(A[i:n,i])).argmax()
        # align vector row with matrix row
        maxrow = maxrow + i - 1
        maxval = A[maxrow,i]
        if maxval == 0:
            raise Exception('The matrix is not LU factorizable')
        if maxrow > i:
            # rows swap
            A[[i,maxrow]]=A[[maxrow,i]]
            p[[i,maxrow]]=p[[maxrow,i]]
        # computation of the i-th Gauss vector that will be
        # part of the L matrix
        A[i+1:,i] = A[i+1:,i]/A[i,i]
        # recomputation of the square sub-matrix defined under
        # the i-th row and after the i-th column
        A[i+1:,i+1:] = A[i+1:,i+1:] - A[i+1:,i]*A[i,i+1:]
    return (A,p)


if __name__ == '__main__':
    A = np.matrix(' 0 41 53 12 62 26;'
                  '43 49 61 60 22 27;'
                  '65 25 56 38 43 43;'
                  '37  0 24 42 26 56;'
                  '26 28 41 15 42 24;'
                  '13 50 48 36 46 28 ')
    # Computation of LU matrices
    B, p = palu_factor(A)
    
    pass