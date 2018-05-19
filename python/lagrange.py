import numpy as np
import matplotlib.pyplot as plt

def lagrange(x, xpoints, ypoints):
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
            if i != j:
                L[i,] = L[i,] * (x - xpoints[j])/(xpoints[i]-xpoints[j])
    y = np.zeros(np.shape(x))
    for i in range(n):
        y = y + ypoints[i]*L[i,]
    return y

def lagrange_int(x, xpoints, ypoints):
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
    L = np.ones((n,np.shape(x)[0]), int)
    for i in range(n):
        for j in range(n):
            if i != j:
                L[i,] = L[i,] * (x - xpoints[j])/(xpoints[i]-xpoints[j])
    y = np.zeros(np.shape(x), int)
    for i in range(n):
        y = y + ypoints[i]*L[i,]
    return y

# Self test
if __name__ == '__main__':
    x = np.array([1, 2, 5])
    y = np.square(x)
    xx = list(range(0,100,1))
    yy = lagrange(xx, x, y)
    # Plot the result
    plt.scatter(xx, yy, linewidth=0.02)
    plt.plot(x, y)
    plt.show()
