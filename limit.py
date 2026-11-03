import sympy as smp
from sympy import *

x = smp.symbols('x') # declare variables

f1 = smp.sin(x) / x 

limit_1 = smp.limit(f1, x, 0) # limit(function, var, approching)

print(f"the limit1 as the limit goes to 0 is {limit_1}")

f2 = 1 / x

limit_2 = smp.limit(f2, x, smp.oo, dir= '+') # you can set the approch from using dir = '+' o '-'

print(f"the limit2 as the limit goes to infiniy is {limit_2}")
