# QR factorization algorithm

import numpy as np
from linalg.triangular import triangular

def qr_factor_in(A):
    (m, n) = A.shape
    for i in range(0,n):
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
    R = qr_factor_in(A)
    Q = R
    return (Q,R)

if __name__ == '__main__':
    # Overdetermined matrix
    A = np.matrix('-1 -1  1;'
                  ' 1  3  3;'
                  '-1 -1  5;'
                  ' 1  3  7 ', float)
    (Q,R) = qr_factor(A)
    print(Q)
    print(R)
