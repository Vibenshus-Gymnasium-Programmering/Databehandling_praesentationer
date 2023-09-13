# [[file:Introduktion_til_sympy.org::*Numeriske løsninger][Numeriske løsninger:2]]
import sympy as sp
x = sp.Symbol("x")
ligning = sp.Eq(sp.exp(x),x+2)
startgaet = [-2,1] # Her gemmes de samme startgæt som i forrige script
loesninger = []
for gaet in startgaet: # Der itereres over alle startgæt
    loesning = sp.nsolve(ligning, x, gaet)
    loesninger.append(loesning)
sp.pprint(loesninger)
# Numeriske løsninger:2 ends here
