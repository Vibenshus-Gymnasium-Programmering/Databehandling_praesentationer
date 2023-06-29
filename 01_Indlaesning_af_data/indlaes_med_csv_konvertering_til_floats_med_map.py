# [[file:01_Indlaesning_af_data_csv_pandas.org::*Indlæsning samt konvertering][Indlæsning samt konvertering:2]]
import csv

tider = []  # Liste som skal indeholde alle tider i float
temperaturer = []  # Liste som skal indeholde alle temperaturer i float
with open("Afkoeling_af_kaffe_nul_grader_udenfor.csv") as datafil:
    csv_laeser = csv.reader(datafil, delimiter=",")
    next(csv_laeser)  # Springer første linje over
    for linje in csv_laeser:
        # map kører funktionen float på alle elementer i linje.
        # list sørger for at gøre det til en liste med floats i.
        # listen indhold udpakkes til variablerne tid og temperatur
        tid, temperatur = list(map(float, linje))

        # tid tilføjes til enden af listen tider
        tider.append(tid)
        # temperatur tilføjes til enden af listen temperaturer
        temperaturer.append(temperatur)
print(tider)
print(temperaturer)
# Indlæsning samt konvertering:2 ends here
