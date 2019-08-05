import matplotlib.pyplot as plt
import numpy as np


def p1(x):
    return (x-1.0)**6

def p2(x):
    return x**6 - 6*(x**5) + 15*(x**4) - 20*(x**3) + 15*(x**2) - 6*x + 1

xx = np.linspace(0.996, 1.004, 81)
plt.plot(xx, [ p1(x) for x in xx ], color='blue')
plt.gcf().text(0.7, 0.9, 'p1', color='blue')
plt.plot(xx, [ p2(x) for x in xx ], color='orange')
plt.gcf().text(0.75, 0.9, 'p2', color='orange')
plt.grid(True)
plt.show()
