# [[file:02_Plot_af_data.org::*To plots i samme vindue med to forskellige y-akser][To plots i samme vindue med to forskellige y-akser:1]]
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
lineaer_farve = "blue"
plt.style.use("seaborn-v0_8")
fig, ax1 = plt.subplots(layout="constrained")
fig.suptitle("Kaffens temperatur som funktion af tiden")
ax1.plot(tider, temperaturer, ".", label="Kaffetemperatur", color=lineaer_farve)
ax1.set_xlabel("Tid [min]")
ax1.set_ylabel(r"Temperatur [${}^\circ C$]")
ax1.grid(False)
ax1.tick_params("y", labelcolor=lineaer_farve)

semilog_farve = "red"
ax2 = ax1.twinx()
ax2.plot(tider, temperaturer, ".", label="Kaffetemperatur semilog", color=semilog_farve)
ax2.set_ylabel(r"Temperatur [${}^\circ C$]")
ax2.set_yscale("log")
ax2.grid(False)
ax2.tick_params("y", labelcolor=semilog_farve)
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
plt.show()
# To plots i samme vindue med to forskellige y-akser:1 ends here
