# PA=LU factorization algorithm

def palu_factor(A):
    '''
    Input:
      - A: a numpy coefficient square matrix
    Output:
      - A: LU factorized matrix with the upper trianguar part
           containing U and the lower trianguar part (diagonal
           excluded) containing L.
      - p: permutation vector
    '''
    # Get the matrix size
    n = A.shape[0]
    p = list(range(0, n))
    if n != A.shape[1]:
        raise Exception('The coefficient matrix should be square')
    for i in range(0,n-1):
        # Get the max row number
        maxrow = abs(A[i:n,i]).argmax()
        # align vector row with matrix row
        maxrow = maxrow + i
        maxval = A[maxrow,i]
        if maxval == 0:
            raise Exception('The matrix is not LU factorizable')
        if maxrow > i:
            # rows swap
            A[[i,maxrow]]=A[[maxrow,i]]
            #p[[i,maxrow]]=p[[maxrow,i]]
            p[i], p[maxrow] = p[maxrow], p[i]
        # computation of the i-th Gauss vector that will be
        # part of the L matrix
        A[i+1:,i] = A[i+1:,i]/A[i,i]
        # recomputation of the square sub-matrix defined under
        # the i-th row and after the i-th column
        A[i+1:,i+1:] = A[i+1:,i+1:] - A[i+1:,i]*A[i,i+1:]
    return (A,p)