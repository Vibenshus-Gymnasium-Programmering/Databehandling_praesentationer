import matplotlib.pyplot as plt
import sympy as sp

x = sp.Symbol("x")
temp_som_funk_af_tid = 90 * 0.975**x
plot_1 = sp.plot(
    temp_som_funk_af_tid,
    (x, -1, 180),
    show=True,
    xlabel="tid[min]",
    ylabel="Temp[grader celsius]",
    yscale="linear",
    legend=True,
    title="Kaffetemperatur som funktion af tiden",
)
