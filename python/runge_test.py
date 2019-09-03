import math

from lagrange import lagrange
from lebesgue import lebesgue_const
import matplotlib.pyplot as plt
import numpy as np


# Runge example function
def runge_func(x):
    return 1.0/(1.0 + x**2)

# Returns a list of equidistant nodes over [a,b]
def equis_nodes(a, b, n):
    return np.linspace(a, b, n)

# Returns a list of n Chebyshev nodes over [a,b]
def cheby_nodes(a, b, n):
    # Chebyscev nodes over the interval [-1,1]
    l = [ math.cos((2*x+1)*math.pi/(2*n)) for x in range(0, n) ]
    # Affine transformation to the interval [a,b]
    return [ (a+b)/2.0 + (b-a)/2.0 * x for x in l ]

#
# Configurations
#
minpoints, maxpoints = 5, 17    # min and max number of nodes
ibeg, iend = -5, 5              # interval begin and end
step = 4
func = runge_func

#get_nodes = equis_nodes
get_nodes = cheby_nodes

xx = np.linspace(ibeg, iend, 100)
yy = [ func(x) for x in xx ]
for n in range(minpoints, maxpoints+1, step):
    _, ax = plt.subplots()
    ax.plot(xx, yy)
    xpoints = get_nodes(ibeg, iend, n)
    ypoints = [ func(x) for x in xpoints ]
    yy1 = lagrange(xpoints, ypoints, xx)
    ax.plot(xx, yy1)
    ax.scatter(xpoints, ypoints, s=15, color='black')
    ax.text(0.2, 0.9, 'n={}'.format(n),
            fontsize=20, transform=plt.gcf().transFigure)
    # Print Lebesgue constant
    lamb = lebesgue_const(xx, xpoints)
    print("n = {:2}   lambda = {}".format(n, lamb))

# Show the graphs
plt.show()
