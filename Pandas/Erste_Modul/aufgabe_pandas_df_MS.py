# 1: DataFrame Erstellung und erste Inspektion

# Erstellt einen Pandas DataFrame mit den folgenden Daten. Nennt ihn buch_verkaeufe.

# | Buchtitel              | Autor         | Genre    | Januar | Februar | März |
# | :--------------------- | :------------ | :------- | :----- | :------ | :--- |
# | Der Ruf des Kuckucks   | Robert Galbraith | Krimi    | 120    | 150     | 130  |
# | Harry Potter und der Stein der Weisen | J.K. Rowling  | Fantasy  | 200    | 180     | 220  |
# | Eine kurze Geschichte der Zeit | Stephen Hawking | Wissenschaft | 80     | 90      | 75   |
# | Stolz und Vorurteil    | Jane Austen   | Klassiker | 95     | 110     | 100  |
# | Die Mitternachtsbibliothek | Matt Haig     | Belletristik | 160    | 170     | 155  |

import pandas as pd
import numpy as np

buch_verkaeufe = pd.DataFrame({
    "Buchtitel":["Der Ruf des Kuckucks", "Harry Potter und der Stein der Weisen","Eine kurze Geschichte der Zeit","Stolz und Vorurteil","Die Mitternachtsbibliothek"],
    "Autor":["Robert Galbraith", "J.K. Rowling","Stephen Hawking","Jane Austen","Matt Haig"],
    "Genre":["Krimi", "Fantasy","Wissenschaft","Klassiker","Belletristik"],
    "Januar":[120,200,80,95,160],
    "Februar":[150,180,90,100,170],
    "März":[130,220,75,100,155]

})


# Zeigt die ersten 3 Zeilen des DataFrames an.
print("------ Ersten 3 Zeilen -------")
print(buch_verkaeufe.head(3))
# print(buch_verkaeufe.iloc[:3],"\n")


# Überprüft die Datentypen der Spalten.
print("------ Datentypen der Spalten ------")
print(buch_verkaeufe.dtypes,"\n")

# Erhaltet eine Zusammenfassung der statistischen Kennzahlen für die numerischen Spalten.
print("------ Statistischen Kennzahlen ------")
print(buch_verkaeufe.describe(),"\n")

# 2: Datenzugriff und Filterung

# Wählt nur die Spalten "Buchtitel" und "Autor" aus und zeigt sie an.
print("------ \"Buchtitel\" und \"Autor\" ------")
print(buch_verkaeufe[["Buchtitel","Autor"]],"\n")

# Filtert den DataFrame, um nur Bücher anzuzeigen, die im Januar mehr als 100 Einheiten verkauft haben.
print("------ Bücher im Januar mehr als 100 ------")
print(buch_verkaeufe.query("Januar>100"),"\n")
# print(buch_verkaeufe.loc[buch_verkaeufe["Januar"]>100])

# Findet alle Fantasy-Bücher und zeigt ihre Titel und Verkaufszahlen für März an.
print("------ Fantasy-Bücher.Titel und Verkaufszahlen für März  ------")
print(buch_verkaeufe.query("Genre =='Fantasy'")[["Buchtitel","März"]],"\n")
# print(buch_verkaeufe[["Buchtitel","März"]].where(buch_verkaeufe["Genre"]=='Fantasy'))

# 3: Neue Spalten und Berechnungen

# print("------ Neue Spalten und Berechnungen  ------")
# buch_verkaeufe["Popular"] = np.where(buch_verkaeufe[["Januar","Februar","März"]].mean(axis=1)>100,"Ja","Nein")
# print(buch_verkaeufe,"\n")

# Berechnet die "Gesamt_Verkaeufe" für jedes Buch über alle drei Monate (Januar, Februar, März) und fügt diese als neue Spalte dem DataFrame hinzu.
print("------ Neue Spalte 'Gesamt_Verkauefe' ------")
# buch_verkaeufe["Gesamt_Verkauefe"] = np.sum(buch_verkaeufe[["Januar","Februar","März"]],axis=1)
buch_verkaeufe["Gesamt_Verkauefe"] = buch_verkaeufe[["Januar","Februar","März"]].sum(axis=1)
print(buch_verkaeufe,"\n")

# Findet das Buch mit den höchsten "Gesamt_Verkaeufe".
print("------ höchsten 'Gesamt_Verkaeufe' ------")
print(buch_verkaeufe.loc[buch_verkaeufe["Gesamt_Verkauefe"].idxmax()],"\n")
# print(buch_verkaeufe["Gesamt_Verkauefe"].max())
# print(buch_verkaeufe["Gesamt_Verkauefe"].max(axis=0))

# 4: Sortieren und Gruppieren
# Sortiert den DataFrame absteigend nach den "Gesamt_Verkaeufe".
print("------ Sortiert absteigend nach den 'Gesamt_Verkaeufe' ------")
buch_verkaeufe_sorted = buch_verkaeufe.sort_values("Gesamt_Verkauefe", ascending=False)
print(buch_verkaeufe_sorted,"\n")

# Gruppiert den DataFrame nach "Genre" und berechnet die durchschnittlichen Gesamtverkäufe pro Genre.
print("------ Gruppiert nach \"Genre\" und berechnet durchschnitt Gesamtverkäufe pro Genre ------")
print(buch_verkaeufe.groupby("Genre",observed=False).agg({"Gesamt_Verkauefe":"mean"}))
