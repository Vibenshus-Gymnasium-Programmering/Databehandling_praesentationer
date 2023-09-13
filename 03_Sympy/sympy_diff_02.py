# [[file:Introduktion_til_sympy.org::*Differentialregning][Differentialregning:2]]
import sympy as sp
x = sp.Symbol("x")
f = (3*x**2 - sp.sqrt(x))/(2+x)
#fm står for f mærke
fm = sp.Derivative(f,x)
print("Viser bare at vi vil differentiere:")
sp.pprint(fm)
# Hvis man gerne vil udføre differentiationen kan man anvende metoden
# .doit()
print("Her er resultatet af differentiationen:")
sp.pprint(fm.doit())
# Differentialregning:2 ends here
