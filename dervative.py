import sympy as smp
from sympy import *


def first():
    x = smp.symbols('x')

    f1 = x**3

    deriv_1 = smp.diff(f1, x)

    print(f"the drivative of x^3 is {deriv_1}")

    f2 = smp.atan(x)

    deriv_2 = smp.diff(f2, x)

    print(f"the drivative of atanx is {deriv_2}")


def main():
    x = smp.symbols('x')
    f, g = smp.symbols('f g', cls = smp.Function) # using cls lets the lib know that those are functions

    g = g(x)
    f = f(x + g)

    ddx = smp.diff(f, x)
    print(f"derivative with the chain rule is {ddx}")

if __name__ == "__main__":
    main()