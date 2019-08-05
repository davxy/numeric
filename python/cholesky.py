def cholesky(A):
    '''
    Cholesky LL^T factorization.

    Input:
      A : input matrix
    Output
      L : lower triangular matrix (such that A=L*L^T)
    '''
    L = [[0.0] * len(A) for _ in xrange(len(A))]
    for i in xrange(len(A)):
        for j in xrange(i+1):
            s = sum(L[i][k] * L[j][k] for k in xrange(j))
            L[i][j] = sqrt(A[i][i] - s) if (i == j) else \
                      (1.0 / L[j][j] * (A[i][j] - s))
    return L
