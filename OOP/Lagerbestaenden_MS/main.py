from produkt import Produkt
from lager import Lager

p1 = Produkt("Laptop", "LP001", 537.5, 3)
p2 = Produkt("Maus", "M2507", 11, 7)
p3 = Produkt("Tastatur", "T0045", 7.37, 5)

print(*list(p.anzeigen_details() for p in (p1,p2,p3)))   #details anzeigen

# for p in (p1,p2,p3):
#     print(p.anzeigen_deteils())

print(p1.produkt_verkaufen(1)) #genügte Menge
print(f"\n{p2.produkt_verkaufen(15)}\n") #ungenügte Menge 

p3.bestand_auffuellen(5)
print(f"\nNach dem Ausfühlung:\n{p3.anzeigen_details()}")

my_lager = Lager()

my_lager.produkt_hinzufuegen(p1)
my_lager.produkt_hinzufuegen(p2)
my_lager.produkt_hinzufuegen(p3)

print("-"*30)
print("Produkte in Lager:")
print(*my_lager.alle_produkte_anzeigen())