# [[file:01_Indlaesning_af_data_csv_pandas.org::*Simpel indlæsning af datafil][Simpel indlæsning af datafil:1]]
import csv

with open("Afkoeling_af_kaffe_nul_grader_udenfor.csv") as datafil:
    csv_laeser = csv.reader(datafil, delimiter=",")
    for linje in csv_laeser:
        print(linje)
# Simpel indlæsning af datafil:1 ends here
