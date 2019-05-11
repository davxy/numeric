# LU factorization algorithm

def lu_factor(A):
    '''
    LU Factorization algorithm

    Input:
      - A: a numpy coefficient square matrix
    Output:
      - A: LU factorized matrix with the upper trianguar part
           containing U and the lower trianguar part (diagonal
           excluded) containing L.
    '''
    # Get the matrix size
    n = A.shape[0]
    if n != A.shape[1]:
        raise Exception('The coefficient matrix should be square')
    for i in range(0,n-1):
        if A[i,i] == 0:
            raise Exception('The matrix is not LU factorizable')
        # computation of the i-th Gauss vector that will be
        # part of the L matrix
        A[i+1:,i] = A[i+1:,i]/A[i,i]
        # recomputation of the square sub-matrix defined under
        # the i-th row and after the i-th column
        A[i+1:,i+1:] = A[i+1:,i+1:] - A[i+1:,i]*A[i,i+1:]
    return A