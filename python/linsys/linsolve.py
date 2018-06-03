import numpy as np
from rref import rref
from diag import diag_solve


def linsolve_diag(M, b):
    rows = len(M)
    d = []
    for i in range(rows):
        d.append(M[i][i])
    return diag_solve(d, b)

def linsolve_rref(M, b):
    rows = len(M)
    cols = len(M[0])
    if rows != len(b):
        return None
    R = []
    for i in range(rows):
        R.append(M[i] + [ b[i] ])
    R = rref(R)
    x = []
    for i in range(rows):
        x.append(R[i][cols])
    return x


def linsolve(M, b, opts=[]):
    if 'D' in opts:
        x = linsolve_diag(M, b)
    else:
        x = linsolve_rref(M, b)
    return x


# Self-test
if __name__ == '__main__':
    '''
    Square cohefficient matrix solution test using Gauss/Jordan elimination.
    '''
    A = [[ 1, 2, -1],
         [ 2, 3, -1],
         [-2, 0, -3]]
    
    b = [-4, -11, 22]

    x = linsolve(A, b)
    print(x)

    # Check the solution using numpy
    A = np.array(A)
    x = np.array(x)
    b = np.array(b)
    if np.allclose(np.dot(A, x), b) != True:
        raise Exception("Solution not correct...")

    '''
    Diagonal cohefficient matrix solution test
    '''

    A = [ [-3,  0, 0],
          [ 0, 21, 0],
          [ 0,  0, 7]]

    b = [-4, -11, 22]

    x = linsolve(A, b, ['D'])
    print(x)

    # Check the solution using numpy
    A = np.array(A)
    x = np.array(x)
    b = np.array(b)
    if np.allclose(np.dot(A, x), b) != True:
        raise Exception("Solution not correct...")
