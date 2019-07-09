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
