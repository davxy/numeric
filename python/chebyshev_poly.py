import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.chebyshev import Chebyshev, cheb2poly


mindeg, maxdeg = 0, 5

cmap = plt.get_cmap('rainbow')
colors = cmap(np.linspace(0, 1, maxdeg-mindeg+1))
print(colors)

l = list(np.zeros(mindeg, int)) + [1]
xx = np.linspace(-1, 1, 100)
tx = 0.2
for i,col in zip(range(mindeg,maxdeg+1),colors):
    c = Chebyshev(l)
    print('T({}) = {}'.format(i, cheb2poly(c.coef)))
    yy = [ c(x) for x in xx ]
    #col = colors.pop()
    plt.gcf().text(tx, 0.9, 'T({})'.format(i), color=col)
    tx += 0.1
    plt.plot(xx, yy, color=col)
    l.insert(0,0)   # increment the degree
plt.grid(True)
plt.show()

