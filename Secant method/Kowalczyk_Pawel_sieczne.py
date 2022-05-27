import math
import numpy as np

def function(x):
    return np.sin(x*x - x + 1/3) + 0.5*x

def Kowalczyk_Pawel_sieczne(x1,x2,eps):
    xk = x1
    xm = x2
    xn = (function(xk)*xm - function(xm)*xk)/(function(xk) - function(xm))
    # k = 1, m = k+1, n = k+2
    while (xn - xm) > eps:
        xk=xm
        xm=xn
        xn=(function(xk)*xm - function(xm)*xk)/(function(xk) - function(xm))
    return xn

