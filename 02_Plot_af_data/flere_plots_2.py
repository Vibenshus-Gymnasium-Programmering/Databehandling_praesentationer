# [[file:02_Plot_af_data_matplotlib.org::*Flere plots på én figur][Flere plots på én figur:2]]
import csv

import matplotlib
import matplotlib.pyplot as plt

tider = []  # Liste som skal indeholde alle tider i float
temperaturer = []  # Liste som skal indeholde alle temperaturer i float
with open("Afkoeling_af_kaffe_nul_grader_udenfor.csv") as datafil:
    csv_laeser = csv.reader(datafil, delimiter=",")
    next(csv_laeser)  # Springer første linje over
    for linje in csv_laeser:
        # På højre side af lighedstegnet anvendes en list comprehension
        # hvor hvert element omdannes til float
        # På venstre side udpakkes den nye liste til variablerne tid og temperatur
        tid, temperatur = [float(element) for element in linje]

        # Tid og temperatur tilføjes til listerne tider og temperaturer
        tider.append(tid)
        temperaturer.append(temperatur)

# Denne del sørger for plot af data
plt.style.use("seaborn-v0_8")
fig, axs = plt.subplots(2, 2, layout="constrained")
fig.suptitle("Kaffens temperatur som funktion af tiden")
print(axs)
for ax in axs.flatten():
    ax.plot(tider, temperaturer, ".", label="Kaffetemperatur")
    ax.set_xlabel("Tid [min]")
    ax.set_ylabel(r"Temperatur [${}^\circ C$]")
    ax.legend()
axs[0, 0].set_title("Lineære akser")
axs[0, 1].set_title("Lineær x-akse. Logaritmisk y-akse.")
axs[0, 1].set_yscale("log")
axs[1, 0].set_title("Logaritmisk x-akse. Lineær y-akse.")
axs[1, 0].set_xscale("log")
axs[1, 1].set_title("Logaritmiske x- og y-akser.")
axs[1, 1].set_xscale("log")
axs[1, 1].set_yscale("log")
plt.show()
# Flere plots på én figur:2 ends here
