import pandas as pd

df = pd.DataFrame({
    "Name": ["Anna", "Ben", "Clara", "David", "Eva"],
    "Alter": [23, 29, 21, 34, 27],
    "Stadt": ["Berlin", "Hamburg", "Berlin", "München", "Köln"],
    "Punkte": [88, 92, 77, 95, 85]
})

# print(df)

# 1. Gib mit .loc die Zeile der Person „Clara“ aus.
df.loc[df["Name"] == "Clara"]

print("#1# ",df.loc[df["Name"] == "Clara"],"\n")

# 2. Gib mit .iloc die zweite Zeile (Ben) aus.
df.iloc[1]

print("#2# ",df.iloc[1],"\n")


# 3. Gib mit .loc die Spalten „Name“ und „Punkte“ für die Personen Anna und David aus.
# print(df.loc[df["Name"] == "David",["Name","Punkte"]],"\n")
df.loc[(df["Name"]=="David")|(df["Name"]=="Anna"), ["Name","Punkte"]]

df.loc[df["Name"].isin(["Anna","David"]),["Name","Punkte"]]

print("#3# ",df.loc[df["Name"].isin(["Anna","David"]),["Name","Punkte"]],"\n")

# 4. Gib mit .iloc die letzten drei Zeilen aus.
df.iloc[-3:]

print("#4# ",df.iloc[-3:],"\n")

# 5. Ändere mit .loc den Punktestand von Eva auf 90.
#Bedienung, dann Spalte
print("#5# ",df[df["Name"]=="Eva"])

df.loc[df["Name"]=="Eva", "Punkte"] = 90
print(df[df["Name"]=="Eva"],"\n")

# 6. Wähle alle Zeilen aus, in denen die Stadt „Berlin“ ist (mit .loc).
df.loc[df["Stadt"]=="Berlin",:]
       
print("#6# ",df.loc[df["Stadt"]=="Berlin"],"\n")

# 7. Wähle mit .iloc alle Werte aus den Spalten 1 und 3 (Alter und Punkte).
print("#7# ",df.iloc[:,[1,3]],"\n")

# 8. Gib mit .loc alle Personen aus, die älter als 25 sind.
print("#8# ",df.loc[df["Alter"]>25],"\n")

# 9. Gib mit .iloc jede zweite Zeile aus (Index 0, 2, 4).
print("#9# ",df.iloc[::2],"\n")

# 10. Gib mit .loc nur die Namen der Personen aus, deren Punktezahl höher als 85 ist.
print("#10# ",   df.loc[df["Punkte"]>85,"Name"]   ,"\n")

print("-"*30)