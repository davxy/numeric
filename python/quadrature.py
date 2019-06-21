
def quad_trapez(a, b, f, n):
    '''
    Composite quadrature using trapezoid method. 

    Input
      a : integration interval start
      b : integration interval end
      f : function reference
      n : number of segments
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
