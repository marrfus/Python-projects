
from fahrzeug import Fahrzeug
from auto import Auto

lis = [Fahrzeug("VW",100), Auto("Volvo", 130,5), Fahrzeug("Skoda", 90), Auto("ZAZ", 60,2)]
print(f"Anzahl von erstellte objekte: {Fahrzeug.anzahl_fahrzeuge}")
print("_"*30)
for f in lis:
    print(f.beschleunigen(10))