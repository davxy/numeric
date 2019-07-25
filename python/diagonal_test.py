# Diagonal linear system solver test

from diagonal import diagonal
import numpy as np


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
