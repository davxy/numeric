# Triangular linear system solver

import numpy as np


def triangular(A, b, typ):
    '''
    Input:
      - A: triangular matrix
      - b: known terms vector
      - typ: 0 if upper, 1 if lower
    Output:
      - x: solution vector
    '''
    n = len(b)
    x = np.empty([n,1])
    if typ == 1:
        start = 0
        stop  = n
        step  = 1
    else:
        start = n-1
        stop  = -1
        step  = -1
    for i in range(start,stop,step):
        x[i] = b[i]
        for j in range(start,i,step):
            x[i] = x[i] - A[i,j]*x[j]
        x[i] = float(x[i]) / A[i,i]
    return x