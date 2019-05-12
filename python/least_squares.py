# Least squares interpolation

import numpy as np
from qr_factor import qr_factor
from triangular import triangular

def least_squares(x, y, d, X):
    '''
    Least squares polynomial
    
    Input:
      - x : x-axis known values
      - y : y-axis known values
      - d : degree of polynomial you want to use
      - X : query points x axis
    Output:
      - Y : values of the least squares polynomial at the query points
    '''
    n = d + 1
    # Build the Vandermonde matrix
    A = np.ones((len(x), n))
    for i in range(1, n):
        A[:,i] = x * A[:,i-1]
    # QR factorization
    (Q, R) = qr_factor(np.asmatrix(A))
    # Least squares vector is vector z such that T*z = g1
    g = Q.T * np.asmatrix(y).T
    g1 = g[0:n]
    T = R[0:n,0:n]
    p = triangular(T, g1, 0)
    # Evaluation of polynomial in query points
    Y = np.polyval(np.flip(p, 0), X)
    return Y
