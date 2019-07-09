from lebesgue import lebesgue_func
import matplotlib.pyplot as plt
import numpy as np
import math

def run_test(a, b, xpoints):
    xx = np.linspace(a, b, 100*len(xpoints))
    yy = [ lebesgue_func(x, xpoints) for x in xx ]
    # Plot the lebesgue function and constant
    _, ax = plt.subplots()
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

# Script
a,b,n = -1.0,1.0,10
equid_test(a,b,n)
cheby_test(a,b,n)
plt.show()
