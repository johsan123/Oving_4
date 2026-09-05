import pandas as pd

df = pd.read_csv("load_data.csv",parse_dates=["Time(Local)"])
print(df.head())
