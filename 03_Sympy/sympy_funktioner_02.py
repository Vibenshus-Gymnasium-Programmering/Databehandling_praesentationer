# [[file:Introduktion_til_sympy.org::*Funktioner][Funktioner:2]]
import sympy as sp
x = sp.Symbol("x")
x_vaerdier = [-5,-2,-1,1,4,7]
f = x**2+x-2
funktionsvaerdier = [f.subs(x, x_vaerdi) for x_vaerdi in x_vaerdier]
sp.pprint(funktionsvaerdier)
# Funktioner:2 ends here
