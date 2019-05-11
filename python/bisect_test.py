# Bisection method root finding tests

from bisect import bisect
from math import sin,cos,exp
import numpy as np

# Get machine precision
eps = np.finfo(float).eps

################################################################################

print('-----------------------------------------------------------------------')
print('f(x) = sin(x)-cos(x)^2')
f = lambda x: sin(x)-cos(x)**2
x,steps = bisect(-1,1,f,eps)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,f(x)))

################################################################################

print('-----------------------------------------------------------------------')
print('f(x) = x^2-8*x+2')
f = lambda x: x**2-8*x+2
x,steps = bisect(0,5,f,eps)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,f(x)))

################################################################################

print('-----------------------------------------------------------------------')
print('f(x) = 2**x-cos(x+3)**2+exp(x+2)')
f = lambda x: 2**x-(cos(x+3))**2+exp(x+2)
x,steps = bisect(-10,10,f,eps)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,f(x)))
