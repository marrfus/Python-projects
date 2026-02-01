import pandas as pd
import numpy as np
import csv
import seaborn as sns
import matplotlib.pyplot as plt


### 1 Daten laden und vorbereiten (Pandas & NumPy) ###
#Daten laden

df = pd.read_csv("Covid Data.csv")

print(df.head())
print("-"*30)
print(f"\nShape: {df.shape}\n")
print("\nTypes:")
print(df.dtypes)

#Fehlende und redundante Werte:
df[["DATE_DIED","INTUBED","PREGNANT","ICU"]] = (
    df[["DATE_DIED","INTUBED","PREGNANT","ICU"]]
    .replace({97:np.nan,99:np.nan})
)
# print(df.isnull().sum())

df["SEX"] = df["SEX"].replace({97:np.nan,99:np.nan})
print(df.isnull().sum())
df.dropna(subset=["SEX"],inplace=True)

#Kategorische Konvertierung (astype)
df[["SEX", "PATIENT_TYPE", "CLASIFFICATION_FINAL","PNEUMONIA","DIABETES"]] = df[["SEX", "PATIENT_TYPE", "CLASIFFICATION_FINAL","PNEUMONIA","DIABETES"]].astype("category")
print(f"\nTypes with category type:\n{df.dtypes}")

#Binäre Spalte erstellen
conditions = [
    df["DATE_DIED"] == "9999-99-99",
    df["DATE_DIED"] != "9999-99-99",
]
choices = [0, 1]
df["DECEASED"] = np.select(conditions,choices)
print("\nNew column 'DESCEASED':")
print(df.DECEASED.head())

### 2: Analyse und Transformation (Gruppierung und Kategorisierung) ###
# Altersgruppen (pd.cut)
intervals = [0,20,40,60,df["AGE"].max()+1]  
categories = ["Kinder/Jugendliche", "Jüngere Erwachsene", "Mittlere Erwachsene", "Ältere Erwachsene"]
df["Age_Group"] = pd.cut(df.AGE, bins=intervals, labels=categories, ordered=True, right=False)


#Mortalität nach Geschlecht und Alter (groupby + mean)
mortality_by_group = (df.groupby(
    ["SEX","Age_Group"],
    observed=False).agg(mort_mean=("DECEASED","mean"))
    .reset_index()
    )
print(mortality_by_group)

#Häufigkeit chronischer Erkrankungen (groupby + count)
# df_confirm_covid = df.loc[df["CLASIFFICATION_FINAL"] <= 3]
# print(df_confirm_covid.head())

# Nur bestätigte Fälle (1,2,3)
# df['CLASIFFICATION_FINAL'].astype("int")
df_confirm = df.query("(CLASIFFICATION_FINAL == 3)|(CLASIFFICATION_FINAL == 2)|(CLASIFFICATION_FINAL == 1)")
df_conf_gr = df_confirm.groupby(["DIABETES","HIPERTENSION"], observed=False)
num_of_cases = df_conf_gr.size().reset_index(name="Count")
print(num_of_cases)

### 3: Visualisierung (Matplotlib & Seaborn) ###
#Verteilung der Fälle (Seaborn)
fig, axs =plt.subplots(1,2)

sns.histplot(df.AGE, bins = 200, ax=axs[0])
axs[0].set_title("Verteilung der 'AGE'")

sns.barplot(x="Age_Group", y="mort_mean", hue="SEX", data=mortality_by_group, ax=axs[1])
axs[1].set_title("Mortalitätsraten")
# axs[1].plot.legend(title="SEX", labels=["Männlich", "Weiblich"])

plt.show()

