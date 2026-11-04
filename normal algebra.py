import sympy as smp
from sympy import *

def factor():
    x,y = smp.symbols('x y')
    f = x**2 + 2*x*y + y**2
    expr = smp.factor(f)
    print(expr)

def expand():
    x,y = smp.symbols('x y')
    f = (x + y)**2
    expr = smp.expand(f)
    print(expr)

def simplify():
    x,y = smp.symbols('x y')
    f = (x**2)/x
    expr = smp.simplify(f)
    print(expr)

def partial_fractions():
    x,y = smp.symbols('x y')
    f = 1/((x**2)+x)
    expr = smp.apart(f)
    print(expr)

partial_fractions()
    