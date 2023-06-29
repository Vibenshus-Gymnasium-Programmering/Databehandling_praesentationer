# [[file:01_Indlaesning_af_data_csv_pandas.org::*Indlæsning vha =DictReader=][Indlæsning vha =DictReader=:1]]
import csv

data = {"Tid": [], "Temperatur": []}
with open("Afkoeling_af_kaffe_nul_grader_udenfor.csv") as datafil:
    csv_laeser = csv.DictReader(datafil, fieldnames = ("Tid", "Temperatur"))
    next(csv_laeser)
    for linje in csv_laeser:
        data["Tid"].append(float(linje["Tid"]))
        data["Temperatur"].append(float(linje["Temperatur"]))
print(data["Tid"])
print(data["Temperatur"])
# Indlæsning vha =DictReader=:1 ends here
