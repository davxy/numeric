from math import ceil,log2,sin,cos
import numpy as np


def bisect(a,b,f,tolx):
    ''' 
    Root finding Bisection method
    
    Input:
      %   - a : confidence interval start
      %   - b : confidence interval end
      %   - f : function reference
      %   - tolx : x axis max tolerance
    Output:
      - x : root approximation
      - steps : required steps
    '''
    imax = ceil(log2(b-a)-log2(tolx))
    for i in range(0,imax):
        x = (a + b)/2
        fa = f(a)
        fb = f(b)
        fx = f(x)
        f1x = abs((fb-fa)/(b-a))
        if (abs(fx) <= tolx*f1x):
            break
        elif (fa*fx < 0):
            b = x
        else: # fa*fx > 0
            a = x
    return (x,i+1)


def print_data(fstr, x, steps, err):
    print(" f(x)={}\n x={}\n steps={}\n err={}\n".format(fstr, x,steps,err))

# Self test
if __name__ == '__main__':
    # Get machine precision
    eps = np.finfo(float).eps

    f = lambda x: np.e**(x/10)-1
    x,steps = bisect(-2,1,f,eps)
    err = abs(f(x))
    print_data('e^(x/10)-1',x,steps,err)

    f = lambda x: sin(x)-cos(x)**2
    x,steps = bisect(-1,1,f,eps)
    err = abs(f(x))
    print_data('sin(x)-cos(x)^2',x,steps,err)

    f = lambda x: x**2-8*x+2
    x,steps = bisect(0,5,f,eps)
    err = abs(f(x))
    print_data('x^2-8*x+2',x,steps,err)
