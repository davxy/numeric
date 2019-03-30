from newton import newton, newton_aitken, newton_chord, newton_secant
from math import sin,cos,exp,log
import numpy as np


# Get machine precision
eps = np.finfo(float).eps

print('-----------------------------------------------------------------------')
print(' f(x) = 2^x-cos(x+3)^2+exp(x+2)')
f  = lambda x: 2**x-(cos(x+3))**2+exp(x+2)
f1 = lambda x: 2**x*log(2)+2*cos(x+3)*sin(x+3)+exp(x+2)
print('> Newton plain')
x,steps = newton(0,f,f1,eps,1000,1)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))
print('> Newton chords')
x,steps = newton_chord(0,f,f1,eps,1000)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))
print('> Newton secant')
x,steps = newton_secant(0,f,f1,eps,1000)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))

print('-----------------------------------------------------------------------')
print(' f(x) = log(sin(x+4)-cos(x-1))-exp(3*x-x^2)')
f  = lambda x: log(sin(x+4)-cos(x-1))-exp(3*x-x**2)
f1 = lambda x: (cos(x+4)+sin(x-1))/(sin(x+4)-cos(x-1))-exp(3*x-x**2)*(3-2*x)
print('> Newton plain')
x,steps = newton(4,f,f1,eps,100,1)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))

print('-----------------------------------------------------------------------')
# 90 iterations to converge... too many for a quadratic method,
# Maybe the root has multiplicity > 1?
print(' f(x) = (4+log(x))*x*(log(x))^3')
f  = lambda x: (4+log(x))*x*(log(x))**3
f1 = lambda x: (log(x)**2)*((log(x)**2)+8*log(x)+12)
print('> Plain Newton')
x,steps = newton(4,f,f1,eps,100,1)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))
# With Aitken acceleration: 5 iterations
print('> Aitken acceleration')
x,steps = newton_aitken(4,f,f1,eps,100)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))
# The root multiplicity should be 3, lets test the plain Newton method with
# known root multiplicity: 6 iterations
print('> Passing the root multiplicity to plain Newton (m=3)')
x,steps = newton(4,f,f1,eps,100,3)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))
# Quasi-Newton method: chords
print('> Newton chords')
x,steps = newton_chord(4,f,f1,eps,5000)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))
# Quasi-Newton method: secant
print('> Newton secant')
x,steps = newton_secant(4,f,f1,eps,5000)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))

print('-----------------------------------------------------------------------')
# The following function root computation with the plain Newton method is
# very inefficient. With 5000 steps the method converges with an error ~5E-7.
# Indeed the root has infinite multiplicity.
print('> Infinite multiplicity root')
print(' f(x) = sin(x-1)-0.5*sin(2*(x-1))')
f  = lambda x: sin(x-1)-0.5*sin(2*(x-1))
f1 = lambda x: cos(x-1)-0.5*x*cos(2*(x-1))
print('> Newton plain')
x,steps = newton(3,f,f1,eps,5000,1)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))
# Same experiment but with Aitken acceleration
print('> Aitken acceleration')
[x,steps] = newton_aitken(3,f,f1,eps,5000)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))
# Quasi-Newton method: chord
print('> Newton chord')
x,steps = newton_chord(3,f,f1,eps,5000)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))
# Quasi-Newton method: secant
print('> Newton secant')
x,steps = newton_secant(3,f,f1,eps,5000)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))

print('-----------------------------------------------------------------------')
# Even with a not so small error tolerance the plain Newton method takes too
# many steps to converge.
print(' f(x) = (3*x-9)^7')
f  = lambda x: (3*x-9)**7
f1 = lambda x: 7*x*(3*x-9)**6
print('> Newton plain')
[x,steps] = newton(8,f,f1,1e-11,300,1)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))
# The root multiplicity is clearly 7
print('> Passing the root multiplicity to plain Newton (m=7)')
[x,steps] = newton(8,f,f1,1e-11,300,7)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))
# Quasi-Newton method: chord
print('> Newton chord')
x,steps = newton_chord(8,f,f1,1e-11,5000)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))
# Quasi-Newton method: secant
print('> Newton secant')
x,steps = newton_secant(8,f,f1,1e-11,5000)
print(" x = {}\n steps = {}\n error = {}".format(x,steps,abs(f(x))))
