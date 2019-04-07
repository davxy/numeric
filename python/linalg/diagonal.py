# Diagonal system solver
import numpy as np

# Diagonal system solver
def diagonal(D, b):
    '''
    input:
      - D: vector with matrix diagonal elements
      - b: known terms vector
    output:
      - x : result vector
    '''
    dlen = len(D)
    if dlen != len(b):
        raise Exception("Error: input vectors lengths mismatch")
    x = list(range(dlen))
    for i in list(range(dlen)):
        x[i] = float(b[i])/D[i]
    return x


# Usage example
if __name__ == '__main__':
    D = [3,5,7,3,1,7,9,10,1,2]
    b = [4,8,1,4,3,9,10,12,11,7]
    x = diagonal(D, b)
    # Prepare the data for assertion below
    A = np.asmatrix(np.diag(D))
    x = np.asmatrix(x).transpose()
    b = np.asmatrix(b).transpose()
    print(A)
    print(x)
    print(b)
    if np.allclose(b, A*x) == False:
        raise Exception('Diagonal test failure')
