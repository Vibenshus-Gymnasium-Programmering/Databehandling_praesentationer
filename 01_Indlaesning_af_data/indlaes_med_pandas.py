# [[file:01_Indlaesning_af_data_csv_pandas.org::*Indlæsning af data vha pandas][Indlæsning af data vha pandas:1]]
import pandas

# df står for dataframe
df = pandas.read_csv("Afkoeling_af_kaffe_nul_grader_udenfor.csv")
# Omdøber kolonnerne til Tider og Temperaturer
df.columns = ["Tider", "Temperaturer"]
# Det kan ses, at tider og temp allerede er konverteret til floats
print(df.dtypes)
# Man kan få fat i kolonnerne på samme måde som i et dictionary
print(df["Tider"])
print(df["Temperaturer"])
# Indlæsning af data vha pandas:1 ends here
