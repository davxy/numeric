#from lagrange import lagrange, lagrange_int
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import numpy as np
import math

def split(n, base):
    digs = []
    while n:
        digs.append(n % base)
        n = math.floor(n / base)
    return digs

def poly_eval(x, digs):
    y = 0
    for i in range(len(digs)):
        y += digs[i] * x**i
    return y

def poly_list_eval(xlist, digs):
    return [ poly_eval(x, digs) for x in xlist ]


k = 3
b = 10000

m = 1234567890123456789012
n = 987654321987654321098

# Step1: Splitting
lm = math.floor(math.log(m,b)/k)
ln = math.floor(math.log(n,b)/k)
i = max(lm,ln)+1
# Polynomial base
B = b**i
# Do the split
p_digs = split(m, B)
q_digs = split(n, B)

# Step2: Evaluation
x = [0, 1, -1, -2,32]

py = poly_list_eval(x, p_digs)
qy = poly_list_eval(x, q_digs)

# Step3: Pointwise multiplication
ry = [a*b for  a,b in zip(py,qy)]

# Step4: Interpolation
#res2 = lagrange([B], np.array(x), np.array(ry))
#res2 = int(res2)
poly = lagrange(np.array(x),np.array(ry))
Polynomial(poly).coef

pass