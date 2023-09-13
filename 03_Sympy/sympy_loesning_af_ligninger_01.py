# [[file:Introduktion_til_sympy.org::*Algebraiske løsninger][Algebraiske løsninger:1]]
import sympy as sp
x = sp.Symbol("x")
# Gemmer ligning 1
ligning_1 = sp.Eq(3*x-2*(x+1), 2)
loesning_1_med_solve = sp.solve(ligning_1, x)
sp.pprint(loesning_1_med_solve)
loesning_1_med_solveset = sp.solveset(ligning_1, x)
sp.pprint(loesning_1_med_solveset)
# Algebraiske løsninger:1 ends here
