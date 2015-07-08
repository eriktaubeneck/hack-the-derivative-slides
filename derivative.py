# coding: utf-8
def eps(x):
    machine_eps = float(max(1, x))
    while float(max(1, x)) + machine_eps != float(max(1, x)):
        last = machine_eps
        machine_eps = machine_eps / 2.
    return last
from scipy.misc import derivative
derivative(lambda x: x**2, 0.)
derivative(lambda x: x**2, 1.)
derivative(lambda x: x**2, 1.e10)
derivative(lambda x: x**2, 1.e100)
e = eps(1.)
e
derivative(lambda x: x**2, 1., e)
derivative(lambda x: x**2, 1.e10, e)
derivative(lambda x: x**2, 1.e100, e)
def df(f, x):
    return derivative(f, x, eps(x))
df(lambda x: x**2, 1.)
df(lambda x: x**2, 1.e10)
df(lambda x: x**2, 1.e100)
def error(f, g, x):
    return abs(df(f, x) - g(x))
error(lambda x: x**2, lambda x: 2*x, 1.)
error(lambda x: x**2, lambda x: 2*x, 1.e10)
error(lambda x: x**2, lambda x: 2*x, 1.e100)
def error_percent(f, g, x):
    return error(f, g, x) / x
error_percent(lambda x: x**2, lambda x: 2*x, 1.)
error_percent(lambda x: x**2, lambda x: 2*x, 1.e10)
error_percent(lambda x: x**2, lambda x: 2*x, 1.e100)
#really error_ratio
import cmath
def cdf(f, x):
    return f(x+eps(x)*1.j).imag / eps(x)
cdf(lambda x: x**2, 1.)
cdf(lambda x: x**2, 1.e10)
cdf(lambda x: x**2, 1.e100)
def cerror(f, g, x):
    return abs(cdf(f, x) - g(x))
cerror(lambda x: x**2, lambda x: 2*x, 1.)
cerror(lambda x: x**2, lambda x: 2*x, 1.e10)
cerror(lambda x: x**2, lambda x: 2*x, 1.e100)
cerror(lambda x: cmath.cos(x), lambda x: cmath.sin(x), 1.)
cerror(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.)
error(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.)
cerror(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.e10)
error(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.e10)
cerror(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.e100)
error(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.e100)
eps(1.e100)
1.e100 + eps(1.e100)
1.e100 + eps(1.e100)*1.j
cmath.cos(1.e100 + eps(1.e100)*1.j)
cmath.cos(1.e100 + eps(1.)*1.j)
cmath.cos(1.e100 + eps(1.)*1.j).imag /eps(1.)
def cdf(f, x):
    return f(x + eps(1.)*1.j).imag / eps(1.)
error(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.e100)
cerror(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.e100)
error(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.)
cerror(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.)
error(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.e10)
cerror(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.e10)
error(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.e100)
cerror(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.e100)
f = lambda x: cmath.exp(x) / cmath.sqrt(x) 
g = lambda x: (cmath.exp(x) * cmath.sqrt(x) - cmath.exp(x) / 2 * cmath.sqrt(x)) / x
error(f, g, 1.)
cerror(f, g, 1.)
cerror(f, g, 1.e10)
error(f, g, 1.e10)
error(f, g, 1.e4)
error(f, g, 1.e3)
error(f, g, 1.)
error(f, g, 10.)
cerror(f, g, 10.)
f(10.)
f(100.)
g(1.)
g(10.)
cdf(f, 10.)
df(f, 10.)
error(cmath.exp, cmath.exp, 1.)
cerror(cmath.exp, cmath.exp, 1.)
cerror(cmath.exp, cmath.exp, 1.e10)
error(cmath.exp, cmath.exp, 1.e10)
exp
import math
error(math.exp, math.exp, 1.e10)
error(math.exp, math.exp, 1.e1)
error(cmath.exp, cmath.exp, 1.e1)
cerror(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.e-100)
error(lambda x: cmath.cos(x), lambda x: -cmath.sin(x), 1.e-100)
