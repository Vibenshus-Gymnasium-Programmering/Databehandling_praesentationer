# [[file:01_Indlaesning_af_data_csv_pandas.org::*Indlæsning af data vha CSV][Indlæsning af data vha CSV:1]]
import csv

with open("Afkoeling_af_kaffe_nul_grader_udenfor.csv") as datafil:
    csv_laeser = csv.reader(datafil, delimiter=",")
    for linje in csv_laeser:
        print(linje)
# Indlæsning af data vha CSV:1 ends here
