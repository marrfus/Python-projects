import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Aufgabe 1: Dataset laden und Überblick verschaffen
df = sns.load_dataset("titanic")
print(f"Original DF:\n{df.head()}\n")

# Aufgabe 2: Eine Kopie erstellen mit .copy()
df_working = df.copy()
print(f"Copied DF:\n{df_working.head()}\n")

# Aufgabe 3: Einzigartige Werte finden mit .unique()
print(f"Unique 'embarked' values:\n{df_working["embarked"].unique()}")

# Aufgabe 4: Häufigkeiten zählen mit .value_counts()
print(f"Häufigkeit der verschiedenen Werte in der Spalte class:")
print(df_working["class"].value_counts())

# Aufgabe 5: Daten gruppieren und zusammenfassen mit .groupby() und .agg()
grouped_results = (df_working
                   .groupby(["sex","pclass"])
                   .agg(avg_age=("age","mean"),
                        avg_price=("fare","mean"),
                        total_survived=("survived","sum")
                        )
                    .reset_index()
                    )
print(df_working["age"].value_counts())
print("Gruppierte Daten:")
print(grouped_results)

# Aufgabe 6: Altersgruppen erstellen mit .cut()
df_working["age"].fillna(df_working.age.mean(),inplace=True)
# df_working["age"] = int(df_working["age"])
# df_working["age"] = df_working["age"].astype(int)
df_working["age"] = round(df_working["age"],2)
intervals = [0,12,18,60,100]
categories = ["Child", "Teenager", "Adult", "Senior"]
df_working["age_group"] = pd.cut(df_working.age, bins=intervals,labels=categories, right=False)
# print(df_working.head())
print("Kategorisierung:")
print(df_working[["age", "age_group"]].head(10))

#age ist float!!!!

#Bonus-Aufgabe
# df_working.groupby(["age_group","survived"],observed=False).value_counts().unstack()
df_gr = df_working.groupby("age_group",observed=False)["survived"].value_counts(normalize=True).unstack()

#ohne normalize
# df_gr = df_working.groupby("age_group",observed=False)["survived"].value_counts().unstack()

print(df_gr)
# .value_counts(normalize=True)


df_gr.plot(kind="barh")
plt.show()
