import pandas as pd

df = pd.read_csv("problembeispiel_Produkt_kauft.csv",delimiter=";")

df = df.drop(columns=["kunde","Unnamed: 4"])

print(df.head())

def gini(series):
    probs = series.value_counts(normalize = True)
    return  1- (probs ** 2).sum()

print(gini(df["Kauf"]))

groups = df.groupby("Alter")

for name, group in groups:
    print(name)
    print(group)


def weighted_gini(df, feature, target):
    total = len(df)
    gini_total = 0

    for value, group in df.groupby(feature):
        weight = len(group)/total
        gini_group = gini(group[target])

        gini_total += weight * gini_group
    return gini_total

features = ["Alter", "Einkommen"]

for feature in features:
    score = weighted_gini(df, feature,"Kauf")
    print(feature, ":" ,score)

def best_split(df, features, target):
    best_feature = None
    best_score = float("inf")

    for feature in features:
        score = weighted_gini(df, feature, target)

        if score < best_score:
            best_score = score
            best_feature = feature
    
    return best_feature, best_score

feature , score = best_split(df, features, "Kauf")

print("Bestes Feature:" , feature)
print("Gini:" ,score)

# CSV laden
# DataFrame analysieren
# Gini / Enropie berechnen
# Feature-Splits testen
# Decision Tree trainieren

from sklearn.tree import DecisionTreeClassifier
X = df[["Alter","Einkommen"]]
y = df["Kauf"]

X_encoded = pd.get_dummies(X)

print(X_encoded)
print(y)
model = DecisionTreeClassifier(criterion="gini")
model.fit(X_encoded,y)


from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plot_tree(model, feature_names=X_encoded.columns, class_names=True)
plt.show()
