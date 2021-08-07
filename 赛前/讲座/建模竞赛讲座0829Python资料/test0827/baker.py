from numpy import pi
from numpy import sin
from numpy import exp
from numpy import array


def tstf(x):
    # z = sin(pi * x)
    z = exp(-x) * sin(pi * x)
    # z = 3 * (x + 0.8) * x * (x - 0.8)
    return z


def le2(x):
    z = 1.5 * x ** 2 - 0.5
    return z


def le3(x):
    z = 2.5 * x ** 3 - 1.5 * x
    return z


def le4(x):
    z = 4.375 * x ** 4 - 3.75 * x ** 2 + 0.375
    return z


def phi(x):
    z = array([[1, x, le2(x), le3(x), le4(x)]])
    z = z.T
    return z
