import matplotlib.pyplot as plt
import numpy as np
import math

def lebesgue_func(x, xpoints):
    n = len(xpoints)
    sums = 0.0
    for i in range(n):
        L = 1.0
        for j in range(n):
            if i == j:
                continue
            L *= float(x - xpoints[j])/float(xpoints[i]-xpoints[j])
        sums += abs(L)
    return sums


def lebesgue_const(xx, xpoints):
    yy = [ lebesgue_func(x, xpoints) for x in xx ]
    return max(yy)


###############################################################################
# Tests
###############################################################################

def run_test(a, b, xpoints):
    xx = np.linspace(a, b, 100*len(xpoints))
    yy = [ lebesgue_func(x, xpoints) for x in xx ]
    # Plot the lebesgue function and constant
    fig, ax = plt.subplots()
    ax.plot(xx, yy)
    ax.text(0.1, 0.9, 'nodes lambda={:.3f}'.format(max(yy)),
            fontsize=18, transform=plt.gcf().transFigure)
    ax.grid(True)

def equid_nodes(a, b, n):
    return np.linspace(a, b, n)

def cheby_nodes(a, b, n):
    xx = [math.cos((2*x+1)*math.pi/(2*n)) for x in range(0,n)]
    return [ (a+b)/2.0 + (b-a)/2.0 * x for x in xx ]

# Test n equidpaced points
def equid_test(a, b, n):
    xpoints = equid_nodes(a, b, n)
    run_test(a, b, xpoints)

# Test n Chebyshev nodes
def cheby_test(a, b, n):
    xpoints = cheby_nodes(a, b, n)
    run_test(a, b, xpoints)

# Self test
if __name__ == '__main__':
    a,b,n = -1.0,1.0,10
    equid_test(a,b,n)
    cheby_test(a,b,n)
    plt.show()

