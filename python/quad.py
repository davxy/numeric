import numpy as np


def quad_trapezoid(a, b, f, n):
    '''
    Composite quadrature using trapezoid method. 

    Input
      a : integration interval start
      b : integration interval end
      f : function reference
      n : number of segments
    Output
      I : integral estimation
    '''
    if (b <= a):
        raise Exception('Error: interval start must be less than interval stop')
    h = (b - a)/n
    x = a
    s = f(a)
    for _ in range(0, n-1):
        x += h
        s += 2*f(x)
    s += f(b)
    I = h*s/2
    return I


def quad_simpson(a, b, f, n):
    '''
    Composite quadrature using 1/3 Simpson's method. 

    Input
      a : integration interval start
      b : integration interval end
      f : function reference
      n : number of segments
    Output
      I : integral estimation
    '''
    if (b <= a):
        raise Exception('Error: interval start must be less than interval stop')
    h = (b - a)/n
    x = a
    s = f(x) + 4*f(x+h/2)
    for _ in range(0, n-1):
        x += h
        s += 2*f(x) + 4*f(x+h/2)
    s += f(b)
    I = h*s/6
    return I


def quad_trapezoid_adapt(a, b, f, tol):
    '''
    Composite quadrature using adaptive trapezoid method.

    Input
      a : integration interval start
      b : integration interval end
      f : function reference
      tol: tolerance
    Output
      I : integral estimation
      x : nodes x-axis list
    '''
    I1 = quad_trapezoid(a, b, f, 1)
    I2 = quad_trapezoid(a, b, f, 2)
    if (abs(I1-I2)/3 <= tol):
        I = I2;
        x = [ a, (a+b)/2, b ]
    else:
        I1, x1 = quad_trapezoid_adapt(a, (a+b)/2, f, tol/2)
        I2, x2 = quad_trapezoid_adapt((a+b)/2, b, f, tol/2)
        I = I1 + I2
        x = list(set(x1).union(set(x2)))
    return I, x


def quad_simpson_adapt(a, b, f, tol):
    '''
    Composite quadrature using adaptive Simpson method.

    Input
      a : integration interval start
      b : integration interval end
      f : function reference
      tol: tolerance
    Output
      I : integral estimation
      x : nodes x-axis list
    '''
    I1 = quad_simpson(a, b, f, 1)
    I2 = quad_simpson(a, b, f, 3)
    if (abs(I1-I2)/15 <= tol):
        I = I2;
        x = [ a, (a+b)/2, b ]
    else:
        I1, x1 = quad_simpson_adapt(a, (a+b)/2, f, tol/2)
        I2, x2 = quad_simpson_adapt((a+b)/2, b, f, tol/2)
        I = I1 + I2
        x = list(set(x1).union(set(x2)))
    return I, x


def quad_romberg(a, b, f, n):
    '''
    Romberg quadrature
    
    Input:
      a : integration interval start
      b : integration interval end
      f : function reference
      n : number of rows in Romberg tableau
    Output:
      I : integral estimation
    '''
    r = quad_romberg_tab(a, b, f, n)
    I = r[n-1, n-1]
    return I


def quad_romberg_tab(a, b, f, n):
    '''
    Romberg quadrature table
    
    Input:
      a : integration interval start
      b : integration interval end
      f : function reference
      n : number of rows in Romberg tableau
    Output:
      r : Romberg table containing the integral values
    '''
    if (b <= a):
        raise Exception('Error: interval start must be less than interval stop')
    h = [ (b - a)/2**i for i in range(0, n) ]
    r = np.zeros((n,n))
    r[0,0] = (b - a) * (f(a) + f(b)) / 2
    for i in range(1, n):
        subtotal = 0
        for k in range(1, 2**(i-1)+1):
            subtotal += f(a + (2*k - 1)*h[i])
        r[i,0] = r[i-1,0]/2 + h[i]*subtotal
        for k in range(1, i+1):
            r[i,k] = (4**k * r[i,k-1] - r[i-1,k-1]) / (4**k - 1)
    return r
