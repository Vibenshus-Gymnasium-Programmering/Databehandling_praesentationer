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
fig, ((ax1, ax2, ax3, ax4)) = plt.subplots(1, 4, layout="constrained")
fig.suptitle("Kaffens temperatur som funktion af tiden")
for ax in (ax1, ax2, ax3, ax4):
    ax.plot(tider, temperaturer, ".", label="Kaffetemperatur")
    ax.set_xlabel("Tid [min]")
    ax.set_ylabel(r"Temperatur [${}^\circ C$]")
    ax.legend()
ax1.set_title("Lineære akser")
ax2.set_title("Lineær x-akse. Logaritmisk y-akse.")
ax2.set_yscale("log")
ax3.set_title("Logaritmisk x-akse. Lineær y-akse.")
ax3.set_xscale("log")
ax4.set_title("Logaritmiske x- og y-akser.")
ax4.set_xscale("log")
ax4.set_yscale("log")
plt.show()
