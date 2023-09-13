# [[file:Introduktion_til_sympy.org::*Kombination af sympy og matplotlib][Kombination af sympy og matplotlib:1]]
import matplotlib
import matplotlib.pyplot as plt
import sympy as sp

# Som set tidligere med anvendelse af sympy
x = sp.Symbol("x")


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


# Opretter figur og akse som set tidligere mens vi arbejdede med at plotte i matplotlib
fig, ax = plt.subplots(layout="constrained")

funktion_1 = x**2 - 2 * x + 4
plot_1 = sp.plot(funktion_1, (x, -3, 3), legend=True, show=False)
flyt_sp_plot_til_ax(plot_1, ax)

funktion_2 = sp.cos(x**2)
plot_2 = sp.plot(funktion_2, (x, -2, 5), legend=True, show=False)
flyt_sp_plot_til_ax(plot_2, ax)

groent_punkt = (-2, 3)
# Det grønne punkt plottes nu direkte gennem matplotlib i stedet for markers gennem sympy
ax.plot(*groent_punkt, "go")

# Annotationen sker her direkte gennem matplotlib i stedet for gennem sympy
ax.annotate(
    "Her er 'toppunktet'.",
    (1, 3),
    xytext=(0, 2),
    arrowprops={"arrowstyle": "->", "lw": 1},
)

# Her sættes aksetitler, aksegrænser og plottitel direkte i matplotlib i stedet for gennem sympy
ax.set_xlabel("x-aksen")
ax.set_ylabel("y-aksen")
ax.set_xlim(-5, 7)
ax.set_ylim(-3, 6)
ax.set_title("En med næsten det hele, tak\nMatplotlib + sympy")

# Endelig plottes hele figuren gennem matplotlib
plt.show()
# Kombination af sympy og matplotlib:1 ends here
