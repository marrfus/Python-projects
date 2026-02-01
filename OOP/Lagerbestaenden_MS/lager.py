class Lager:
    def __init__(self):
        self.produkte = []

    def produkt_hinzufuegen(self, produkt):
        self.produkte.append(produkt)

    def alle_produkte_anzeigen(self):
        return (p.anzeigen_details() for p in self.produkte)