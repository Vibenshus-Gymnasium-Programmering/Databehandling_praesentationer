# [[file:Introduktion_til_sympy.org::*Kombination af sympy og matplotlib][Kombination af sympy og matplotlib:2]]
import csv
import matplotlib.pyplot as plt
import sympy as sp

# Standard sympy
x = sp.Symbol("x")


# Denne funktion kender I fra sympyeksemplet fra tidligere
def flyt_sp_plot_til_ax(sp_plot, ax):
    """Denne funktion tager et sympy-plot og en matplotlib ax som parameter,
    og sørger for at indsætte sympy-plottet i det allerede eksisterende ax."""
    backend = sp_plot.backend(sp_plot)
    backend.ax = ax
    backend._process_series(backend.parent._series, ax, backend.parent)
    backend.ax.spines["right"].set_color("none")
    backend.ax.spines["bottom"].set_position("zero")
    backend.ax.spines["top"].set_color("none")
    plt.close(backend.fig)


# Dette kender næsten fra tidligere fra matplotlibeksemplerne
kaffedata = [[], []]
with open("Afkoeling_af_kaffe_nul_grader_udenfor.csv") as datafil:
    csv_laeser = csv.reader(datafil, delimiter=",")
    next(csv_laeser)  # Springer første linje over
    for linje in csv_laeser:
        # På højre side af lighedstegnet anvendes en list comprehension
        # hvor hvert element omdannes til float
        # På venstre side udpakkes den nye liste til variablerne tid og temperatur
        tid, temperatur = (float(element) for element in linje)

        # Tid og temperatur tilføjes til listerne tider og temperaturer
        kaffedata[0].append(tid)
        kaffedata[1].append(temperatur)

# Standard fra matplotlib
fig, ax = plt.subplots(layout="constrained")

# Lidt forskellige funktioner som alle skal plottes
funktioner = [0.1 * (x - 100) ** i + 10 * i for i in range(1, 5)]

for funktion in funktioner:
    plot = sp.plot(funktion, (x, 0, 180), legend=True, show=False)
    flyt_sp_plot_til_ax(plot, ax)


# Plotter kaffedata
ax.plot(*kaffedata, ".", label="Kaffetemperatur")


# Laver en ekstra dataserie og plotter den
ekstra_dataserie = [range(0, 180, 10), [10 * 1.01**i for i in range(0, 180, 10)]]
ax.plot(*ekstra_dataserie, "go", label="Ekstra dataserie")


# Vil gerne pege på et helt specielt punkt
specielt_punkt = (40, 60)
ax.annotate(
    f"Her er det helt specielle punkt {specielt_punkt}",
    specielt_punkt,
    xytext=(20, 70),
    arrowprops={"arrowstyle": "->", "lw": 1},
)

# Standard matplotlib
ax.set_title("En blanding af det hele.")
ax.set_xlabel("Tid [min]")
ax.set_ylabel(r"Temperatur [${}^\circ C$]")
ax.set_xlim(0, 180)
ax.set_ylim(-10, 120)
ax.legend()
plt.show()
# Kombination af sympy og matplotlib:2 ends here
