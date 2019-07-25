from bisect import bisect

from newton import newton
import numpy as np


# Get machine precision as tolx
tolx = np.finfo(float).eps

print('f(x) = x^3 - 5x')
f  = lambda x: x**3 - 5*x
f1 = lambda x: 3*x**2 - 5

print('> Try with Newton')
x,steps = newton(1,f,f1,tolx,1000,1)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))
if abs(f(x)) > tolx*abs(f1(x)):
    print('> Non-convergence detected, fallback to Bisection')
    x,steps = bisect(-10,1,f,tolx)
    print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))
