# Bisection root finding method

from math import ceil,log2

def bisect(a,b,f,tolx):
    ''' 
    Bisection root finding method
    
    Input:
        - a    : confidence interval start
        - b    : confidence interval end
        - f    : function reference
        - tolx : x axis max tolerance
    Output:
        - x     : root approximation
        - steps : required steps (i+1)
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