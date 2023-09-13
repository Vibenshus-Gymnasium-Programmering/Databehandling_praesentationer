# [[file:Introduktion_til_sympy.org::*Direkte med sympy][Direkte med sympy:2]]
import sympy as sp
x = sp.Symbol("x")
funktion_1 = x**2
funktion_2 = x**3 -x +2

sp.plot(funktion_1, funktion_2, (x,-3, 3), legend=True)
# Direkte med sympy:2 ends here
