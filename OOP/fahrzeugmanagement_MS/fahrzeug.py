
class Fahrzeug:
    anzahl_fahrzeuge = 0

    def __init__(self, marke, geschwindigkeit):
        self.__marke = marke
        self.__geschwindigkeit = geschwindigkeit
        Fahrzeug.anzahl_fahrzeuge += 1

    @property
    def marke(self):
        return self.__marke
    
    @marke.setter
    def marke(self, neue_marke):
        self.__marke = neue_marke
    
    @property
    def geschwindigkeit(self):
        return self.__geschwindigkeit
    
    @marke.setter
    def geschwindigkeit(self, neue_geschwindigkeit):
        self.__geschwindigkeit = neue_geschwindigkeit
    
    #Instanzmethode
    def beschleunigen(self, wert):
        self.__geschwindigkeit += wert
        return f"Das Fahrzeug {self.__marke} beschleunigt."

    @classmethod
    def gesamtbestand_pruefen(cls):
        return cls.anzahl_fahrzeuge