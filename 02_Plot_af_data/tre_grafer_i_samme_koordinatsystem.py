# [[file:02_Plot_af_data_matplotlib.org::*Flere grafer i samme koordinatsystem][Flere grafer i samme koordinatsystem:1]]
import csv

import matplotlib
import matplotlib.pyplot as plt

tider = []  # Liste, som skal indeholde alle tider i float
# Lister, som skal indeholde temperatuerne for hver af de 3 kaffer
temperaturer_1 = []
temperaturer_2 = []
temperaturer_3 = []

with open("tre_afkoelingskurver.csv") as datafil:
    csv_laeser = csv.reader(datafil, delimiter=",")
    next(csv_laeser)  # Springer første linje over
    for linje in csv_laeser:
        # På højre side af lighedstegnet anvendes en list comprehension
        # hvor hvert element omdannes til float
        # På venstre side udpakkes den nye liste til de viste variable
        tid, temp_1, temp_2, temp_3 = [float(element) for element in linje]

        # Tid og temperatur tilføjes til listerne tider og temperaturer
        tider.append(tid)
        temperaturer_1.append(temp_1)
        temperaturer_2.append(temp_2)
        temperaturer_3.append(temp_3)

# Denne del sørger for plot af data
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots(layout="constrained")
ax.plot(tider, temperaturer_1, ".", label="Kaffe 1")
ax.plot(tider, temperaturer_2, ".", label="Kaffe 2")
ax.plot(tider, temperaturer_3, ".", label="Kaffe 3")
ax.set_title("Kaffens temperatur som funktion af tiden.")
ax.set_xlabel("Tid [min]")
ax.set_ylabel(r"Temperatur [${}^\circ C$]")
ax.legend()
plt.show()
# Flere grafer i samme koordinatsystem:1 ends here
