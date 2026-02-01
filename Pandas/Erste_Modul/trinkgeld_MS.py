import seaborn as sns
import pandas as pd
import numpy as np

df = sns.load_dataset("tips")
# print(df)
df['tip_percentage']=round(df["tip"]/df["total_bill"]*100)
# print(df)
print(df.head())

# Analyse mit pivot_table:
# ○ Erstellen Sie eine Pivot-Tabelle, die den Wochentag (day) als Index und die 
# Uhrzeit (time) als Spalten verwendet.
# ○ Die Werte (values) sollen das durchschnittliche 'tip' (Trinkgeld) und der 
# durchschnittliche 'tip_percentage' sein.
# ○ Verwenden Sie die Funktion np.mean (oder einfach 'mean') als 
# Aggregationsfunktion.

df_pivot = df.pivot_table(values=["tip","tip_percentage"],
                          index="day", 
                          columns="time", 
                          aggfunc=np.mean)

print(df_pivot)

df_group = df.groupby(["day","time"],observed=False).agg({"tip":"mean","tip_percentage":"mean"})
print(df_group)