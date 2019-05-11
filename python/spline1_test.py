import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-math.pi,math.pi,8) 
y = [math.sin(k) for k in x ]

for i in range(len(x)-1):
    plt.plot([x[i],x[i+1]],[y[i],y[i+1]], color='black')
    plt.scatter([x[i],x[i+1]],[y[i],y[i+1]], color='black')
plt.grid(True)
plt.show()
