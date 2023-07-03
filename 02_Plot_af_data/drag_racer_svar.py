import csv

import matplotlib
import matplotlib.pyplot as plt

tider = []  # Liste som skal indeholde alle tider i float
distancer = []  # Liste som skal indeholde alle temperaturer i float
hastigheder = []
accelerationer = []
with open("drag_racer.csv") as datafil:
    csv_laeser = csv.reader(datafil, delimiter=",")
    next(csv_laeser)  # Springer første linje over
    for linje in csv_laeser:
        # På højre side af lighedstegnet anvendes en list comprehension
        # hvor hvert element omdannes til float
        # På venstre side udpakkes den nye liste til variablerne tid og temperatur
        tid, distance, hastighed, acceleration = [float(element) for element in linje]

        # Tid og temperatur tilføjes til listerne tider og temperaturer
        tider.append(tid)
        distancer.append(distance)
        hastigheder.append(hastighed)
        accelerationer.append(acceleration)

# Denne del sørger for plot af data
distance_farve = "blue"
plt.style.use("seaborn-v0_8")
fig, ax1 = plt.subplots(layout="constrained")
fig.suptitle("Drag racer")
ax1.plot(tider, distancer, ".", label="Afstand", color=distance_farve)
ax1.set_xlabel("Tid [s]")
ax1.set_ylabel("Distance [m]")
# ax1.grid(False)
ax1.grid(True)
ax1.tick_params("y", labelcolor=distance_farve)

hastighed_farve = "red"
ax2 = ax1.twinx()
ax2.plot(tider, hastigheder, ".", label="Hastighed", color=hastighed_farve)
ax2.set_ylabel("Hastighed [m/s]")
ax2.grid(False)
ax2.tick_params("y", labelcolor=hastighed_farve)
fig.legend(loc="upper left", bbox_to_anchor=(0, 1), bbox_transform=ax1.transAxes)
plt.show()
