# Cubic spline interpolation

import numpy as np

def spline3(x, y, X):
    '''
    Cubic Spline interpolation method.

    Input:
      - x  : precomputed points x axis values
      - y  : precomputed points y axis values
      - xq : query points x axis
    Output:
      - yq : interpolation result for query points
    '''
    (a, b, c, d) = spline3_coef(x, y)
    Y = np.zeros(len(X))
    for i in range(0, len(X)):
        Y[i] = spline3_eval(a, b, c, d, x, X[i])
    return Y

def spline3_eval(a, b, c, d, x, Xi):
    '''
    Evaluation function.

    Input:
      - [ a, b, c, d ] : spline coefficients list 
      - x  : precomputed points x axis values
      - Xi : query point
    Output:
      - Yi : spline value at query point
    '''
    i = 0
    while i < len(x)-1 and Xi > x[i+1]:
        i = i+1
    # Xi is between x[i] and x[i+1]
    Yi = a[i]*(Xi-x[i])**3 + b[i]*(Xi-x[i])**2 + c[i]*(Xi-x[i]) + d[i]
    return Yi

def build_tridiag(h, n):
    '''
    Internal helper function to build the trigiagonal matrix used to find
    the unknown values m(i)
    '''
    T = np.zeros((n,n))
    for i in range(0, n):
        T[i,i] = 2*(h[i] + h[i+1])
    for i in range(0, n-1):
        T[i+1,i] = h[i]
        T[i,i+1] = h[i+1]
    return T

def spline3_coef(x, y):
    '''
    Helper function returning a list of coefficients vectors.
    Assumption: x and y shall be of the same length

    Input:
      - x : interpolation nodes x axis values
      - y : interpolation nodes y axis values
    Output:
      - [a,b,c,d] : List of coefficients vectors
        The polynomial used in the interval [x(i), x(i+1)) is constructed as
        Ci(x) = a[i](x-x[i])^3 + b[i](x-x[i])^2 + c[i](x-x[i]) + d[i]
    '''
    n = len(x)
    # Intervals lengths
    h = x[1:n] - x[0:n-1]
    # Divided differences
    dd = (y[1:n] - y[0:n-1]) / h
    # Build the tridiagonal matrix
    T = build_tridiag(h, n-2)
    # System right hand side and solve the system
    rhs = 6*(dd[1:len(dd)] - dd[0:len(dd)-1])
    m = np.linalg.solve(T, rhs)
    # Natural boundary conditions: second derivative is zero at endpoints
    m = np.array([0] + list(m) + [0])
    # Get the coefficients
    d = y
    c = dd - h * (2*m[0:n-1] + m[1:n]) / 6
    b = m/2
    a = (m[1:n] - m[0:n-1]) / (6*h)
    return (a, b, c, d)
