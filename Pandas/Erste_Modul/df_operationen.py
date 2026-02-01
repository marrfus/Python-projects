import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Anna", "Ben", "Clara", "David", "Eva"],
    "Alter": [23, 29, 21, 17, 27],
    "Stadt": ["Berlin", "Hamburg", "Berlin", "München", "Köln"],
    "Punkte": [88, 92, 77, 95, 85]
})

#Alter>30
print(df[df["Alter"]>30])

print(df[(df["Alter"]>30)&(df["Stadt"]=="Berlin")]) #gibt niemandem

print(df[(df["Alter"]>30)|(df["Stadt"]=="Berlin")])  #gibt viele Leute

print(df[~(df["Stadt"]=="Berlin")])    #alle, die nicht in Berlin wochnen
print(df[df["Stadt"]!="Berlin"])    #alle, die nicht in Berlin wochnen2

print(df[df["Name"].str.contains("Anna")])   #Case sensibel
print(df[df["Name"].str.contains("anna",case=False)]) # nicht sensibel, egal ob es große oder kleine Buchstabe

print(df[df["Stadt"].isin(["Berlin","Hamburg"])])  #sucht nach Werte, die in Liste gibt

print(df.loc[df["Alter"].between(25,35)])  #Gränzen gehören auch dazu

df["Erwachsen"] = np.where(df["Alter"]>=18,"Ja", "Nein")
print(df)