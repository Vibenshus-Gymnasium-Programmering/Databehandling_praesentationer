# [[file:02_Plot_af_data_matplotlib.org::*Flere grafer i samme koordinatsystem][Flere grafer i samme koordinatsystem:2]]
import csv

import matplotlib
import matplotlib.pyplot as plt

tider = []  # Liste som skal indeholde alle tider i float
# Dict som skal indeholde en liste af alle temperaturer i float for hver kaffe
temperaturer = {1: [], 2: [], 3: [],}  with open("tre_afkoelingskurver.csv") as datafil:
    csv_laeser = csv.reader(datafil, delimiter=",")
    next(csv_laeser)  # Springer første linje over
    for linje in csv_laeser:
        # På højre side af lighedstegnet anvendes en list comprehension
        # hvor hvert element omdannes til float
        # På venstre side udpakkes den nye liste til variablen tid og listen _temperaturer
        tid, *_temperaturer = [float(element) for element in linje]

        # Tid og temperatur tilføjes til listerne tider og temperaturer
        tider.append(tid)
        for run, temp in zip(temperaturer, _temperaturer):
            temperaturer[run].append(temp)

# Denne del sørger for plot af data
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots(layout="constrained")
for nummer, _temperaturer in temperaturer.items():
    ax.plot(tider, _temperaturer, ".", label=f"Kaffe {nummer}")
ax.set_title("Kaffens temperatur som funktion af tiden.")
ax.set_xlabel("Tid [min]")
ax.set_ylabel(r"Temperatur [${}^\circ C$]")
ax.legend()
plt.show()
# Flere grafer i samme koordinatsystem:2 ends here
