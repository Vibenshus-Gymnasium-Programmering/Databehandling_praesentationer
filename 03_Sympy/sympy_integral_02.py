# [[file:Introduktion_til_sympy.org::*Bestemte integraler][Bestemte integraler:1]]
import sympy as sp
x = sp.Symbol("x")
f = x**3 * (x-1)
bestemt_integral = sp.integrate(f,(x, 1, 2)) # tuplen er (x, 1, 2)
sp.pprint(bestemt_integral)
# Vi vil gerne have svaret i decimaltal
# Vi bruger metoden .evalf()
sp.pprint(bestemt_integral.evalf(4)) # Vi vil kun have 4 betydende cifre
# Vi kan igen blot vise, at vi vil udføre et bestemt integral
bestemt_integral = sp.Integral(f,(x, 1, 2))
sp.pprint(bestemt_integral)
# Vi printer det faktiske integral ud
sp.pprint(bestemt_integral.doit().evalf(4))
# Bestemte integraler:1 ends here
