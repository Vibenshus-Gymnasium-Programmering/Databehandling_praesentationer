# [[file:02_Plot_af_data_plotly.org::+begin_src python -n :exports both :results output :eval never-export :comments link :tangle plotly_simpel.py][No heading:1]]
import csv
import plotly.express as px

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

fig = px.scatter(
    x=tider,
    y=temperaturer,
    labels={"x": "Tid [min]", "y": r"$Temperatur [{}^\circ C]$"},
    title="Kaffetemperatur som funktion af tiden",
)

fig.show()
# No heading:1 ends here
