# [[file:Introduktion_til_sympy.org::*Det basale - Opstilling af udtryk][Det basale - Opstilling af udtryk:1]]
import sympy as sp
# a defineres til at være et symbol
a = sp.Symbol("a")

# Nu oprettes et udtryk
# Læg mærke til at alle gangetegn skal skrives ind.
udtryk_b = (1+a)/(3*(2+1))*2/a
# Nedenfor printes udtrykket ud på en "pæn" måde
sp.pprint(udtryk_b)
# Det basale - Opstilling af udtryk:1 ends here
