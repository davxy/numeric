import numpy as np


def chol_factor(M):
    '''
    Cholesky LL' factorization.

    Input:
      M : input matrix
    Output
      L : lower triangular matrix (such that M=L*L')
    '''
    n = len(M)
    L = np.zeros((n, n))
    for i in range(0, n):
        L[i, i] = np.sqrt(M[i, i] - np.dot(L[i, :],L[i, :]))
        for j in range(i+1, n):
            L[j, i] = (M[j, i] - np.dot(L[i, :],L[j, :])) / L[i, i]
    return L