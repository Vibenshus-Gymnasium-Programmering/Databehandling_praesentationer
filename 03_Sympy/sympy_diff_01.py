# [[file:Introduktion_til_sympy.org::*Differentialregning][Differentialregning:1]]
import sympy as sp
x = sp.Symbol("x")
f = (3*x**2 - sp.sqrt(x))/(2+x)
print("Med funktionen sp.diff")
sp.pprint(sp.diff(f,x,1)) # læg mærke til x og 1 som de sidste argumenter.
print("Med metoden .diff")
sp.pprint(f.diff(x,1)) # Læg mærke til x og 1 som de sidste argumenter.
# Differentialregning:1 ends here
