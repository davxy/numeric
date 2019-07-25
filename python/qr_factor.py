# QR factorization algorithm

import numpy as np


def qr_factor_in(A):
    '''
    QR factorization algorithm working inplace.

    Returns a matrix with the R factor in the upper right corner
    and the Householder's vectors in the lower right part.
    The final Q construction shall be performed by the user.

    Input:
      - A : coefficient matrix.
    Output:
      - A : result matrix.
    '''
    (m, n) = A.shape
    for i in range(0, n):
        alpha = np.linalg.norm(A[i:,i])
        if alpha is 0:
            raise Exception('The matrix does not have maximum rank')
        if A[i,i] > 0:
            alpha = -alpha
        print(alpha)
        v1 = A[i,i] - alpha
        A[i,i] = alpha
        A[i+1:m,i] = A[i+1:m,i]/v1
        # beta = (alpha-z1)/alpha = 2/(u'u)
        #   with u the scaled Householder's vector u=(z-alpha*ei)/(z1-alpha*e1)
        beta = -v1/alpha;
        v = np.insert(A[i+1:m,i], 0, 1, axis=0)
        A[i:m,i+1:n] = A[i:m,i+1:n] - (beta * v) * (v.T * A[i:m,i+1:n])
    return A

def qr_factor(A):
    '''
    QR factorization algorithm
    
    Input:
      - A : coefficient matrix
    Output:
      - Q : first factor
      - R : second factor
    '''
    R = qr_factor_in(A)
    (m, n) = A.shape
    Q = np.matrix(np.identity(m))
    for i in range(0, n):
        v = np.insert(R[i+1:m,i], 0, 1, axis=0)
        H = np.matrix(np.identity(m))
        H[i:m,i:m] = np.matrix(np.identity(m-i)) - 2*(v*v.T)/(v.T*v)
        Q = Q*H
        R[i+1:m,i] = np.zeros((m-i-1,1))
    return (Q, R)