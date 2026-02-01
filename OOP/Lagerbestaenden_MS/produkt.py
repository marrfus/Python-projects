
class Produkt:

    def __init__(self, name:str, produkt_id:str, preis:float, bestand:int):
        self.name = name
        self.produkt_id = produkt_id
        self.preis = preis
        self.bestand = bestand

    def anzeigen_details(self):
        return rf"""
Produkt: {self.name} (ID: {self.produkt_id})
Preis: {self.preis} EUR
Verfügbar: {self.bestand} Stück
"""
    def produkt_verkaufen(self,menge:int):
        if self.bestand>= menge:
            self.bestand -= menge
            return f"{menge} {self.name} verkauft. Neue {self.name} Bestand ist: {self.bestand}."
        else: return f"Nicht genügend {self.name} auf Lager!\nVerfügbar: {self.bestand}.\nVersucht zu verkaufen: {menge}"
        
    def bestand_auffuellen(self, menge):
        self.bestand += menge
