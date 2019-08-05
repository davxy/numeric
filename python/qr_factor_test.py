# QR factorization algorithm

import numpy as np
from qr_factor import qr_factor


# Overdetermined matrix
A = np.matrix('-1 -1  1;'
              ' 1  3  3;'
              '-1 -1  5;'
              ' 1  3  7 ', float)
# QR factorization (deep-copy of A because we need it or the "check")
(Q,R) = qr_factor(np.matrix(A))
# Results check
if np.allclose(A, Q*R) == False:
    raise Exception('QR factorizzation test failure')