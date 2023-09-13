# [[file:Introduktion_til_sympy.org::*Direkte med sympy][Direkte med sympy:1]]
import sympy as sp
x = sp.Symbol("x")
funktion_1 = x**2

sp.plot(funktion_1, (x,-5, 5))
# Direkte med sympy:1 ends here
