# Newton interpolating polynomial

import numpy as np
from divdiff import divdiff

def newton_interp(x, y, X):
    '''
    Newton interpolation method
    Input:
      - x : precomputed points x axis values
      - y : precomputed points y axis values
      - X : query points x axis
    Output:
      - Y : query points y axis (interpolation results)
    '''
    n = len(x)
    Y = np.zeros(len(X))
    for k in range(n):
        L = np.ones(len(X))
        for i in range(k):
            L *= (X - x[i])
        a = divdiff(x[0:k+1], y[0:k+1])
        Y += a*L
    return Y
