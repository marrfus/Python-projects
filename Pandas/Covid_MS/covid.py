import pandas as pd
import numpy as np
import csv
import seaborn as sns
import matplotlib.pyplot as plt


# 1 Daten laden und vorbereiten (Pandas & NumPy)
#Daten laden

df = pd.read_csv("Covid Data.csv")

# Erste Inspektion
print(df.head())
print("-"*30)
print("\nINFO:")
print(df.info())
print(f"\nShape: {df.shape}\n")

#Fehlende Werte behandeln
print("Fehlende Werte")
print(df.isnull().sum())
print(f"\nFehlende Werte in AGE:\n{df["AGE"].isnull().sum()}")

# Es gibt keine fehlende Werte
print("\nMedian:")
print(np.median(df["AGE"])) #40
#df['Age'].median()
df.fillna(df['AGE'].median(),inplace=True)

#Neue Spalte erstellen mit np.select()
conditions = [
    df["AGE"] <= 30,
    df["AGE"].between(31,60),
    df["AGE"] > 60
]
choices = ["Jung", "Mittel", "Senior"]
df["Altersgruppe"] = np.select(conditions, choices, default="unbekannt")#wenn zufällig Age ist None
print(f"\nNeue Spalte 'Altengruppe':\n{df.Altersgruppe.head()}")


# 2 DATENANALYSE
#Gruppierte Analyse
print("-"*30)
print("\nDATENANAYSE\nGruppierte Analyse\n\nNeue Spalte MORTALITY")
#Neue Spalte MORTALITY erstellen mit np.select()
conditions = [
    df["DATE_DIED"] == "9999-99-99",
    df["DATE_DIED"] != "9999-99-99",
]
choices = [0, 1]
df["MORTALITY"] = np.select(conditions,choices)
print(df.MORTALITY.head())
df_gr = df.groupby(["Altersgruppe"]).agg(mort_mean=("MORTALITY","mean"))
print(df_gr)

#Häufigkeitsverteilung

print(df[["SEX", "Altersgruppe"]].value_counts().reset_index())
# pivot = (df.pivot_table(
#         values=   ???,
#         index="Altersgruppe",
#         columns="SEX",
#         aggfunc="sum"
#     ))
# print(pivot)

# 3 Datenvisualisierung (Seaborn & Matplotlib)
fig, axs =plt.subplots(2,2)
# Verteilung einer Variablen (Seaborn):
# sns.histplot(
#     df.AGE,
#     bins = 200,
#     kde=True
#     )
# plt.title("Verteilung der 'AGE'")
# plt.show()
sns.histplot(
    df.AGE,
    bins = 200,
    kde=True,
    ax=axs[0,0]
    )
axs[0,0].set_title("Verteilung der 'AGE'")


#Kategoriale Vergleiche (Seaborn):
#boxplot
# sns.boxplot(x="SEX", y="AGE", data=df)
# plt.xlabel("Gender")
# plt.ylabel("Age")
# plt.title("Boxplot: Age nach Gender")
# plt.show()
sns.boxplot(x="SEX", y="AGE", data=df, ax=axs[1,0])
axs[1,0].set_title("Boxplot: Age nach Gender")

#bar. Anzahl der Fälle für jede Gruppe
# sns.countplot(x="Altersgruppe", data = df, order = ["Jung", "Mittel", "Senior"])
# plt.title("Countplot")
# plt.xlabel("age group")
# plt.ylabel("number of cases")
# plt.show()
sns.countplot(x="Altersgruppe", data = df, order = ["Jung", "Mittel", "Senior"],ax=axs[0,1])
axs[0,1].set_title("Countplot")


#Beziehung zwischen zwei Variablen (Seaborn)

# plt.figure(figsize=(12,10))
# sns.heatmap(df[["AGE","ICU"]].corr(), annot=True, fmt=".2f")
# plt.title("Correlation Heatmap")
# plt.show()
sns.heatmap(df[["AGE","ICU"]].corr(), annot=True, fmt=".2f",ax=axs[1,1])
axs[1,1].set_title("Correlation Heatmap")

plt.show()

#Individuelle Anpassung (Matplotlib)
