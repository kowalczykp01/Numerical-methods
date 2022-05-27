import math
import numpy as np
import matplotlib.pylab as p


def function(x):
    return np.sin(x*x - x + 1/3) + 0.5*x


def Kowalczyk_Pawel_sieczne(x1,x2,eps):
    x = np.arange(-1.5, 0.5, 0.01)
    y = np.sin(x*x - x + 1/3) + 1/2*x
    p.plot(x, y)
    p.plot([x1, x2], [function(x1), function(x2)])
    p.grid(True)
    p.xlabel("x")
    p.ylabel("y = sin(x^2 - x +1/3) + 1/2x")
    xk = x1
    xm = x2
    xn = (function(xk)*xm - function(xm)*xk)/(function(xk) - function(xm))
    # k = 1, m = k+1, n = k+2
    while (abs(xn - xm)) > eps:
        xk = xm
        xm = xn
        p.plot([xk, xm], [function(xk), function(xm)])
        xn = (function(xk)*xm - function(xm)*xk)/(function(xk) - function(xm))
    p.show()
    return xn


x1 = -1.1
x2 = -1.0
eps = 0.00000001

print(Kowalczyk_Pawel_sieczne(x1, x2, eps))
