import seaborn as sns
import pandas as pd
import numpy as np

df = sns.load_dataset("diamonds")

print("\nInfo und aktuellen Speicherverbrauch:")
print(df.info())

print("\nData types:")
print(df.dtypes)

print(f"\n----- Gesamter Speicherbedarf des Datensatzes: -----\n{df.memory_usage(deep=True)}")
print(f"\nInsgesamt besetzt: {df.memory_usage(deep=True).sum()}")

# ohne deep=True
print(f"\n----- OHNE deep: ----- \n{df.memory_usage()}")
print(f"\nOberflächige Speichernutzung: {df.memory_usage().sum()}")

vsp = df.memory_usage(deep=True).sum() / df.memory_usage().sum()
print(f'\nVerhältnis Tatsächlicher zu oberflächlicher Speichernutzung\n{vsp:.4f}\n')

df_opti = df.copy()

# print(f"\nLänge: {len(df)}")
# print("Unique daten ")
# print(df_opti.columns)
for i in df_opti.columns:
    # print(f"{i}: {df[i].unique().size}")
    if df_opti[i].dtype=="float64":
        df_opti[[i]] = df_opti[[i]].apply(pd.to_numeric, downcast="float")
        # print(f"{i} MIN: {df[i].min()}   {i} MAX: {df[i].max()}")
#preis  
# df_opti["price"] = df_opti["price"].astype("uint64")  
# df_opti[["price"]] = df_opti[["price"]].apply(pd.to_numeric, downcast="unsigned")
df_opti[["price"]] = df_opti[["price"]].apply(pd.to_numeric, downcast="integer")
print(f"price MIN: {df["price"].min()}   price MAX: {df["price"].max()}")

print(f"Data Types:\n{df_opti.dtypes}")
print(df_opti.head())

print(f"\nOpti Memory Usage:\n{df_opti.memory_usage(deep=True)}")
print(f"Opti memory usage sum: {df_opti.memory_usage(deep=True).sum()}")

vsp_opti = df.memory_usage(deep=True).sum() / df_opti.memory_usage(deep=True).sum()
print(f'\nVerhältnis Tatsächlicher zu oberflächlicher Speichernutzung\n{vsp_opti:.4f}')

#Reduction
reduction = (df.memory_usage(deep=True).sum()-df_opti.memory_usage(deep=True).sum())/df.memory_usage(deep=True).sum()
print("-"*30)
print(f"\nReduktion um: {reduction*100:0.2f}%")










