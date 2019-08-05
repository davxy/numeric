# Orthogonal linear system solver

import numpy as np


def orthogonal(A, b, chk=0):
    # Optionally chk for orthogonality
    if chk == 1 and is_orthogonal(A) == 0:
        raise Exception('Not orthogonal input matrix')
    return A.transpose()*b

def is_orthogonal(A):
    return np.allclose(A*A.transpose(), np.identity(A.shape[0]))