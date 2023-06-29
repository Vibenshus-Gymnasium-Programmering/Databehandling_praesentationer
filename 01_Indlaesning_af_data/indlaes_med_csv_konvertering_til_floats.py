# [[file:01_Indlaesning_af_data_csv_pandas.org::*Indlæsning samt konvertering][Indlæsning samt konvertering:1]]
import csv

tider = [] # Liste som skal indeholde alle tider i float
temperaturer = [] # Liste som skal indeholde alle temperaturer i float
with open("Afkoeling_af_kaffe_nul_grader_udenfor.csv") as datafil:
    csv_laeser = csv.reader(datafil, delimiter=",")
    next(csv_laeser)  # Springer første linje over
    for linje in csv_laeser:
        tid, temperatur = linje  # listen linje udpakkes
        tid, temperatur = float(tid), float(temperatur)  # konvertering til floats
        tider.append(tid) # Tilføjer den nuværende tid til enden af listen tider
        temperaturer.append(temperatur) # Tilføjer den nuværende temperatur til enden af listen temperaturer

print(tider)
print(temperaturer)
# Indlæsning samt konvertering:1 ends here
