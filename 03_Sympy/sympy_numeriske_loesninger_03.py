# [[file:Introduktion_til_sympy.org::*Numeriske løsninger][Numeriske løsninger:3]]
import sympy as sp
x = sp.Symbol("x")
ligning = sp.Eq(sp.exp(x),x+2)
startgaet = [-2,1] # Her gemmes de samme startgæt som i forrige script
# Her opbygges listen med løsninger vha list comprehension
loesninger = [sp.nsolve(ligning,x,gaet) for gaet in startgaet] 
sp.pprint(loesninger)
# Numeriske løsninger:3 ends here
