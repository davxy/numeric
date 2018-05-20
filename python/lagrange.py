import numpy as np
import matplotlib.pyplot as plt

def lagrange_eval(x, xpoints, ypoints):
    '''
    Lagrange interpolation method
    Input:
        - x : points to evaluate x axis
        - xpoints: precomputed points x axis values
        - ypoints: precomputed points y axis values
    Output:
        - y : interpolated points y axis
    '''
    n = np.shape(xpoints)[0]
    L = np.ones((n,np.shape(x)[0]))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            L[i,] = L[i,] * (x - xpoints[j])/(xpoints[i]-xpoints[j])
    y = np.zeros(np.shape(x),int)
    for i in range(n):
        y = int(y + ypoints[i]*L[i,])
    return y

def lagrange_poly(xpoints, ypoints):
    '''
    Return a Lagrange interpolating polynomial.

    Input
        - x : array-like x-coordinates of a set of datapoints.
        - y : array-like y-coordinates of a set of datapoints, i.e. f(x).
    Output:
        - Lagrange interpolating polynomial as a `numpy.poly1d` instance    """
    '''
    n = len(xpoints)
    p = np.poly1d(0.0)
    for j in range(n):
        pt = np.poly1d(ypoints[j])
        for k in range(n):
            if k == j:
                continue
            pt *= np.poly1d([1.0, -xpoints[k]])/(xpoints[j]-xpoints[k])
        p += pt
    return p

# Self test
if __name__ == '__main__':
    x = np.array([1, 2, 5])
    y = np.square(x)
    xx = list(range(0,100,1))
    yy = lagrange_eval(xx, x, y)
    # Plot the result
    plt.scatter(xx, yy, linewidth=0.02)
    plt.plot(x, y)
    plt.show()

    p = lagrange_poly(x, y)
    pass