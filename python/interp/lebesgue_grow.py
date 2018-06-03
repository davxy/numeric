import matplotlib.pyplot as plt
import numpy as np
import math
from lebesgue import lebesgue_const

def equis_nodes(a, b, n):
    return np.linspace(a, b, n)

def cheby_nodes(a, b, n):
    xx = [math.cos((2*x+1)*math.pi/(2*n)) for x in range(0,n)]
    return [ (a+b)/2.0 + (b-a)/2.0 * x for x in xx ]

# Show how the growth of the Lebesgue constant is bound to the number
# of interpolation nodes for the two cases: equispaced and chebyshev.
def grow_test(a, b, nmax):
    xx = np.linspace(a, b, 100)
    nn = range(1, nmax+1)
    cc_equis = [ lebesgue_const(xx, equis_nodes(a,b,n)) for n in nn ]
    cc_cheby = [ lebesgue_const(xx, cheby_nodes(a,b,n)) for n in nn ]
    # Plot stuff follows...
    plt.semilogy(nn, cc_equis, color='blue')
    plt.semilogy(nn, cc_cheby, color='green')
    plt.xlabel('n')
    plt.ylabel('log(lambda)')
    plt.gcf().text(0.2, 0.95, 'equispaced', color='blue')
    plt.gcf().text(0.2, 0.9, 'chebyshev', color='green')
    plt.grid(True)
    plt.show()


grow_test(-5,5,30)

