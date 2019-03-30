def newton(x,f,f1,tolx,imax,m):
    '''
    Newton root finding method

    Input:
        - x    : first root approximation
        - f    : function reference
        - f1   : first derivative function reference
        - tolx : max tolerance
        - imax : max iterations before stop trying
        - m    : root multiplicity; if unknown set to 1.
    Output:
        - x     : final root approximation
        - steps : required steps (i+1)
    '''
    for i in range(0,imax):
        fx  = f(x)
        f1x = f1(x)
        if (abs(fx) <= tolx*abs(f1x)):
            break
        x = x - m*fx/f1x
    return (x,i+1)


def newton_aitken(x,f,f1,tolx,imax):
    '''
    Newton root finding method with Aitken acceleration
 
    Input:
        - x    : first root approximation
        - f    : function reference
        - f1   : first derivative function reference
        - tolx : max tolerance
        - imax : max iterations before stop trying
    Output:
        - x     : final root approximation
        - steps : required steps (i+1)
    '''
    for i in range(0, imax):
        # 1st point using plain Newton
        fx  = f(x)
        f1x = f1(x)
        if (abs(fx) <= tolx*abs(f1x)):
            break
        x1 = x-fx/f1x
        # 2nd point using plain Newton
        fx  = f(x1)
        f1x = f1(x1)
        if (abs(fx) <= tolx*abs(f1x)):
            x = x1
            break
        x2 = x1-fx/f1x
        # Acceleration step
        x = (x1*x1-x*x2)/(2*x1-x2-x)
    return (x,i+1)


def newton_chord(x,f,f1,tolx,imax):
    '''
    Newton chords root finding method 
 
    Input:
        - x    : first root approximation
        - f    : function reference
        - f1   : first derivative function reference
        - tolx : max tolerance
        - imax : max iterations before stop trying
    Output:
        - x     : final root approximation
        - steps : required steps (i+1)
    '''
    f1x = f1(x)
    for i in range(0,imax):
        fx  = f(x)
        if (abs(fx) <= tolx*abs(f1x)):
            break
        x = x - fx/f1x
    return (x,i+1)


def newton_secant(x,f,f1,tolx,imax):
    '''
    Newton chords root finding method 
 
    Input:
        - x    : first root approximation
        - f    : function reference
        - f1   : first derivative function reference
        - tolx : max tolerance
        - imax : max iterations before stop trying
    Output:
        - x     : final root approximation
        - steps : required steps (i+1)
    '''
    # Compute a second point using the plain Newton method
    fx0  = f(x)
    f1x0 = f1(x)
    x0   = x
    x    = x0 - fx0/f1x0
    for i in range(0,imax):
        fx   = f(x)
        f1x  = f1(x)
        if (abs(fx) <= tolx*abs(f1x) or fx == fx0):
            break
        tmp = x
        x = x - fx*(x-x0)/(fx-fx0)
        x0 = tmp
        fx0 = fx
    return (x,i+1)
