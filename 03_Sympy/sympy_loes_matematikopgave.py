import sympy
from sympy.abc import x

h = 8 * sympy.log(1.5 * x - 2) + 3

hm = sympy.diff(h)

sympy.plot(h, hm, (x, 2, 73))
print(hm.subs(x, 8))
