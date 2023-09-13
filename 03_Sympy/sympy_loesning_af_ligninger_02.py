# [[file:Introduktion_til_sympy.org::*Algebraiske løsninger][Algebraiske løsninger:2]]
import sympy as sp
x = sp.Symbol("x")
# Gemmer ligning 1
ligning_2 = sp.Eq(2/(x+1), 1/(x-1))
loesning_2_med_solveset = sp.solveset(ligning_2, x)
sp.pprint(loesning_2_med_solveset)
# Algebraiske løsninger:2 ends here
