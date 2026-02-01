
# Konfiguriert eine Kundenbestellung.
# - kunden_id: Positioneller Pflicht-Parameter.
# - max_anzahl: Optionaler Parameter mit Standardwert.
# - *produkte: Variable Anzahl von bestellten Produkten.
# - **optionen: Zusätzliche Keyword-Optionen (z.B. 'versandart').

def konfiguriere_bestellung(kunden_id, max_anzahl=10, *produkte,**optionen):

    print(f"ID: {kunden_id}, Max: {max_anzahl}, Produkte: {produkte}, Optionen: {optionen}")


#Anrufe:
#1
print("A1")
konfiguriere_bestellung(1001,5)
#ID: 1001, Max: 5, Produkte: (), Optionen: {}

#2
print("\nA2")
konfiguriere_bestellung(1002,5, "Laptop", "Maus")
#ID: 1002, Max: 5, Produkte: ('Laptop', 'Maus'), Optionen: {}

#3
#konfiguriere_bestellung(1003,"Monitor", "Tastatur",max_anzahl=20)
#TypeError: konfiguriere_bestellung() got multiple values for argument 'max_anzahl'

#4
#konfiguriere_bestellung(kunden_id=1004, 5, "Stift")
#SyntaxError: positional argument follows keyword argument

#5
#konfiguriere_bestellung(1005, versandart="Express", 20)
#SyntaxError: positional argument follows keyword argument

#6
print("\nA6")
konfiguriere_bestellung(max_anzahl=30, kunden_id=1006,artikel="Buch")
#ID: 1006, Max: 30, Produkte: (), Optionen: {'artikel': 'Buch'}

#----------------------------------------------------------------------------

#Teil B
print("-"*30)
print("\nTeil B")
artikel_liste = ["T-Shirt", "Hose", "Schuhe"]
zusatz_details = {"rabatt": 0.15, "filiale": "Online"}

konfiguriere_bestellung(2001,8,*artikel_liste, **zusatz_details)