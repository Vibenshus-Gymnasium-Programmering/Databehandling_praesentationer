# [[file:Introduktion_til_sympy.org::*Direkte med sympy][Direkte med sympy:3]]
import sympy as sp
x = sp.Symbol("x")
funktion_1 = x**2 -2*x+2
funktion_2 = sp.cos(x**2)

sp.plot((funktion_1, (x, -3, 3)), (funktion_2, (x,-2, 5)), legend=True)
# Direkte med sympy:3 ends here
