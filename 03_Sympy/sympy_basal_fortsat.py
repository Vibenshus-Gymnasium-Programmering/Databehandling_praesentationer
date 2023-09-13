# [[file:Introduktion_til_sympy.org::*Tilbage til opgaven][Tilbage til opgaven:1]]
import sympy as sp
# a defineres til at være et symbol
a = sp.Symbol("a")

# Nu oprettes et udtryk
# Læg mærke til at alle gangetegn skal skrives ind.
udtryk_b = (1+a)/(3*(2+1))*2/a
# Nedenfor printes udtrykket ud på en "pæn" måde
print("Oprindeligt udtryk")
sp.pprint(udtryk_b)
print("Forsøg med at omskrive til en enkelt brøk")
sp.pprint(sp.cancel(udtryk_b))
# Tilbage til opgaven:1 ends here
