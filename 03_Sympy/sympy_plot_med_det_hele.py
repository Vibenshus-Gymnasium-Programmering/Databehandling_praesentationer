# [[file:Introduktion_til_sympy.org::*Direkte med sympy][Direkte med sympy:4]]
import sympy as sp
x = sp.Symbol("x")
funktion_1 = x**2 -2*x+4
funktion_2 = sp.cos(x**2) 

sp.plot((funktion_1, (x, -3, 3)),
        (funktion_2, (x,-2, 5)),
        legend=True,
        title= "En med næsten det hele, tak",
        xlabel = "x-aksen",
        ylabel = "y-aksen",
        xlim = (-5,7),
        ylim = (- 3, 6),
        annotations = [{"xy": (1,3), "text": "Her er 'toppunktet'.", "xytext": (0,2), "arrowprops":dict(arrowstyle='->', lw=1)}],
        markers = [{"args":[-2,3, 'go']}],
        )
# Direkte med sympy:4 ends here
