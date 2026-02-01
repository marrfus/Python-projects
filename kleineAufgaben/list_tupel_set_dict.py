# liste []
print("-"*30)
einkaufsliste = ["Äpfel","Brot","Milch"]
print(einkaufsliste)
einkaufsliste.append("Käse")
print(einkaufsliste)
einkaufsliste.remove("Brot")
print("Die endgültige einkaufsliste:\n",einkaufsliste)
print("-"*30)

# tupel ()
berlin_koordinaten = ("52.5200° N","13.4050° E")
print("Berlin Breitengrad: ",berlin_koordinaten[0])
# berlin_koordinaten[0]=0
print("Berlin Koordinaten: ",berlin_koordinaten[0],",",berlin_koordinaten[1])
print("-"*30)

#set {}
rohanmeldungen = ["Anna", "Ben", "Carla", "Anna", "David", "Ben"]
print(rohanmeldungen)
eindeutige_teilnehmer = set(rohanmeldungen)
print(eindeutige_teilnehmer)
eindeutige_teilnehmer.add("Emil")
print(eindeutige_teilnehmer)
print("Carla" in eindeutige_teilnehmer)
if "Carla" in eindeutige_teilnehmer:
    print("Ja, Carla ist da")
else: 
    print("Nein, Carla ist nicht da")
print("Die eindeutige Teilnehmer:\n",eindeutige_teilnehmer)
print("-"*30)

#dictionary
lagerbestand = {"Hammer": 25,"Schrauben": 150,"Säge": 12}
print(lagerbestand)
lagerbestand["Hammer"]-=3
lagerbestand["Bohrer"]=8
print("Schraubenstand: ",lagerbestand["Schrauben"])
print("Letzte: ",lagerbestand)
print("-"*30)

