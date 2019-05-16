# Lagrange interpolating polynomial

import numpy as np

def lagrange_eval(x, y, X):
    '''
    Lagrange interpolation method
    Input:
      - x : precomputed points x axis values
      - y : precomputed points y axis values
      - X : query points x axis
    Output:
      - Y : query points y axis (interpolation results)
    '''
    n = len(x)
    Y = np.zeros(len(X))
    for i in range(n):
        L = np.ones(len(X))
        for j in range(n):
            if i != j:
                L *= (X - x[j])/(x[i]-x[j])
        Y += y[i]*L
    return Y


def lagrange_poly(x, y):
    '''
    Return a Lagrange interpolating polynomial.

    Input
      - x : array-like x-coordinates of a set of datapoints.
      - y : array-like y-coordinates of a set of datapoints, i.e. f(x).
    Output:
      - p: Lagrange interpolating polynomial as a `numpy.poly1d` instance.
    '''
    n = len(x)
    p = np.poly1d(0.0)
    for j in range(n):
        pt = np.poly1d(y[j])
        for k in range(n):
            if k != j:
                pt *= np.poly1d([1.0, -x[k]])/(x[j]-x[k])
        p += pt
    return p
