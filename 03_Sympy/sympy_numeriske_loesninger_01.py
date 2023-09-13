# [[file:Introduktion_til_sympy.org::*Numeriske løsninger][Numeriske løsninger:1]]
import sympy as sp
x = sp.Symbol("x")
ligning = sp.Eq(sp.exp(x),x+2)
loesning_1 = sp.nsolve(ligning,x,-2) # Læg mærke til -2 som sidste argument
sp.pprint(loesning_1)
loesning_2 = sp.nsolve(ligning,x,1) # Læg mærke til 1 som sidste argument
sp.pprint(loesning_2)
# Numeriske løsninger:1 ends here
