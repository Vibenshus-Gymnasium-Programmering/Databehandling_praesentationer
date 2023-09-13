# [[file:Introduktion_til_sympy.org::*Fra streng til udtryk][Fra streng til udtryk:1]]
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

x = sp.Symbol("x")
# t = sp.Symbol("t")

funktionsstreng = "x*exp(cos(x))"
funktion = parse_expr(funktionsstreng)
sp.pprint(funktion)
sp.plot(funktion, (x, -20, 20))
# Fra streng til udtryk:1 ends here
