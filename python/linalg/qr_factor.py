# QR factorization algorithm

import numpy as np
from linalg.triangular import triangular

def qr_factor_in(A):
    (m, n) = A.shape
    for i in range(0,n-1):
        alpha = np.linalg.norm(A[i:,i])
        print(alpha)

if __name__ == '__main__':
    # Overdetermined matrix
    A = np.matrix('-1 -1  1;'
                  ' 1  3  3;'
                  '-1 -1  5;'
                  ' 1  3  7 ', float)
    qr_factor_in(A)
