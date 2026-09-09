import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("load_data.csv",parse_dates=["Time(Local)"])

df["Time(Local)"] = pd.to_datetime(df["Time(Local)"], format="%d.%m.%Y %H:%M:%S %z",utc=True)


df = df.set_index("Time(Local)")



df["Consumption"] = df["Consumption"].str.replace(",",".").astype(float)
df["Production"] = df["Production"].str.replace(",",".").astype(float)


#Oppgave 4
#print(df.head())


#print(df.dtypes)

#Oppgave 5
#print(df.index[0])

#Oppgave 6  
print(df.loc["2026-01-01 03:00"])
print(df.loc["2026-01-01 00:00:00":"2026-01-02 00:00:00"])

Daglig_last = df.loc["2026-01-01 00:00:00":"2026-01-02 00:00:00"]

plt.plot(Daglig_last.index, Daglig_last["Consumption"], label="Consumption")
plt.plot(Daglig_last.index, Daglig_last["Production"], label="Production")
plt.xlabel("Tid")
plt.ylabel("Effekt")
plt.legend()
plt.tight_layout
plt.xticks(rotation=45)
plt.savefig("Daglig_last")
plt.show()

