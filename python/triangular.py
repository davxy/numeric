# Triangular system solver
import numpy as np

def triangular(A, b, typ):
    '''
    input:
      A: triangular matrix
      b: known terms vector
      typ: 0 if upper, 1 if lower
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


if __name__ == "__main__":
    # Lower triangular matrix
    A = np.matrix('12  0  0  0  0;'
                  '18 38  0  0  0;'
                  '51  4 57  0  0;'
                  '53  3  8  2  0;'
                  '31 26 4 16  60', float)
    # Known terms vector
    b = np.matrix('68; 9; 46; 43; 35')
    # Solve the system
    x = triangular(A, b, 1)
    # Check
    if np.allclose(b, A*x) == False:
        raise Exception('Lower triangular test failure')
    
    # Upper triangular matrix
    A = np.matrix('12 48  2 51 49;'
                  ' 0 38 32 51  5;'
                  ' 0  0 57  2 31;'
                  ' 0  0  0  2 53;'
                  ' 0  0  0  0 60', float)
    # Known terms vector
    b = np.matrix('7; 31; 32; 34; 22')
    # Solve the system
    x = triangular(A, b, 0)
    # Check
    if np.allclose(b, A*x) == False:
        raise Exception('Upper triangular test failure')
