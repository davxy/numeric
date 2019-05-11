# Divided differences

def divdiff(x,y):
    '''
    Divided differences using the recursive forward definition.

    Input:
      - x : x values sequence.
      - y : y values sequence (same len as x).
    Ouput:
      - D : divided differences of order n, with n the length of the inputs.
    '''
    n = len(x)
    if n == 1:
        D = y[0]
    else:
        D = (divdiff(x[1:n],y[1:n])-divdiff(x[0:n-1],y[0:n-1]))/(x[n-1]-x[0])
    return D 