import matplotlib.pyplot as plt
import numpy as np

def lebesgue_func(x, xpoints):
    n = len(xpoints)
    sums = 0.0
    for i in range(n):
        L = 1.0
        for j in range(n):
            if i == j:
                continue
            L = L * float(x - xpoints[j])/float(xpoints[i]-xpoints[j])
        sums += L
    return sums


# Self test
if __name__ == '__main__':
    xx = list(np.arange(-1.0,1.0,0.1))
    yy = [ lebesgue_func(x, xx) for x in xx ]
    # Plot the lagrange function with equispaced points
    plt.plot(xx, yy)
    plt.show()

