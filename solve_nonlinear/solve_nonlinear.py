import sympy as sym
from math import *

# in the python session that opens in the terminal, paste the following
r, h = sym.symbols('r,h')

f = sym.Eq((4 * pi * r ** 3) / 3 + h * pi * r ** 2, 4000)
g = sym.Eq(4 * pi * r ** 2, 4 * pi * r * h)

print(sym.solve([f, g], (r, h), set=True))
