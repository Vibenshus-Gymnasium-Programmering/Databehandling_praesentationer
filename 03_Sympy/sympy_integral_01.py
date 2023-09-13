# [[file:Introduktion_til_sympy.org::*Stamfunktioner][Stamfunktioner:1]]
import sympy as sp
x = sp.Symbol("x")
f = x**3 * (x-1)
# Med F menes stamfunktion til f
F = sp.integrate(f,x)
sp.pprint(F)
# Vi viser kun, at vi har tænkt os at integrere
F = sp.Integral(f,x)
sp.pprint(F)
# Vi printer det faktiske integral ud
sp.pprint(F.doit())
# Stamfunktioner:1 ends here
