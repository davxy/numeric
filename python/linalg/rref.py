import numpy as np

def rref(M):
    '''
    Reduce a matrix to its row echelon form.

    Input:
        - M : input matrix
    Output:
        - R : matrix reduced row echelon form
    '''
    R = M[:]    # Deep copy the content
    l = 0       # Lead value index
    rows,cols = R.shape
    for r in range(rows):
        if l >= cols:
            return R
        # Search the row with "leftest" leading value
        i = r
        while R[i,l] == 0:
            i += 1
            if i == rows:
                i = r
                l += 1
                if cols == l:
                    return R
        # Exchange rows
        R[i,r] = R[r,i]
        # Divide by leading value
        R[r] /= R[r,l]
        # Elimination step
        for i in range(rows):
            if i != r:
                R[i] = R[i] - R[i,l]*R[r]
        l += 1
    return R


if __name__ == "__main__":
    # Test if the reduced row echelon function
    A = np.matrix(' 1  2  -1;'
                  ' 2  3  -1;'
                  '-2, 0, -3',
                  float);
    b = np.matrix('-4; -11; 22')

    #
    # Find the inverse first
    #

    # Augmented matrix
    M = np.column_stack((A,np.identity(3)))
    # Transform in row echelon form
    R = rref(M)
    # Extract the inverse
    A1 = R[:,3:6]
    # Test inverse
    if np.allclose(np.identity(3), A*A1) == False:
        raise Exception('Inverse find failure')
    # Test
    x = A1*b
    if np.allclose(b, A*x) == False:
        raise Exception('System resolution test failure')

    #
    # Direct resolution
    #

    # Augmented matrix
    M = np.column_stack((A,b))
    # Transform in row echelon form
    R = rref(M)
    # Check the result
    x = R[:,3]
    # Check
    if np.allclose(b, A*x) == False:
        raise Exception('System resolution test failure')

