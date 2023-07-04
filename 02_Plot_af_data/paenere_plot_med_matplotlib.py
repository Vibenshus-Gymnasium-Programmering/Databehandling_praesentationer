# [[file:02_Plot_af_data_matplotlib.org::*Et lidt pænere plot][Et lidt pænere plot:1]]
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
fig, ax = plt.subplots(layout="constrained")
ax.plot(tider, temperaturer, ".", label="Kaffetemperatur")
ax.set_title("Kaffens temperatur som funktion af tiden.")
ax.set_xlabel("Tid [min]")
ax.set_ylabel(r"Temperatur [${}^\circ C$]")
ax.legend()
plt.show()
# Et lidt pænere plot:1 ends here
