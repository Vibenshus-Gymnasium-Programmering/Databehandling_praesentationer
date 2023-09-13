# [[file:Introduktion_til_sympy.org::*Funktioner][Funktioner:1]]
import sympy as sp
x = sp.Symbol("x")
x_vaerdier = [-5,-2,-1,1,4,7]
f = x**2+x-2
for x_vaerdi in x_vaerdier:
    sp.pprint(f.subs(x, x_vaerdi))
# Funktioner:1 ends here
