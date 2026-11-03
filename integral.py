import sympy as smp
from sympy import *

x = smp.symbols('x')

f = 1/x

integral = smp.integrate(f, x)

print(f"the integral is {integral} + c")