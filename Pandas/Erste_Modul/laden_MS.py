import pandas as pd

#1. DataFrame laden
df = pd.DataFrame({
    "Produkt":["Apfel","Birne","Milch","Käse", "Tomate", "Gurke"],
    "Preis":["1,20","0.90","1.50","2.40","0.70","0.60"],
    "Anzahl":[30,45,20,10,50,40],
    "Kategorie":["Obst","Obst", "Milchprodukte", "Milchprodukte", "Gemüse","Gemüse"]
})

#2. Spaltennamen umbenennen: "Preis" in "price"und "Anzahl" in "quantity"
df = df.rename(mapper={"Preis":"price","Anzahl":"quantity"},axis=1)
print("Renamed: ")
print(df.columns)

#3. Preis zu numerisch
df["price"] = pd.to_numeric(df["price"].str.replace(",","."), downcast="float")
print("\nPrice now float: ")
print(df["price"],"\n")

#4. Neue Spalte berechnen
df["total"] = round(df["price"]*df["quantity"],2)
print(f"Total: \n{df["total"]}")

#5. Filtern mit loc
print(f"Obst: \n{df.loc[df["Kategorie"]=="Obst"]}\n")

#6. Zugriff mit iloc
print(f"3 Zeilen und 3 Spalten:\n{df.iloc[:3,:2]}")  #Zeilen ,  dann Spalten

#7. Höchster Umsatz
print(f"Max Total:  {max(df["total"])}") #nur max total zahl
print(df.loc[df["total"].idxmax()]) #ganze Zeile von max wert

#8. Bonus
df_sorted = df.sort_values("total", ascending=False) #absteigen
print(f"Sorted DF:\n{df_sorted}")







