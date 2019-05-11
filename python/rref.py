# Reduced row echelon form algorithm

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