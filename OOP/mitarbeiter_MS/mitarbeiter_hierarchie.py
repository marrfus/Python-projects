
class Mitarbeiter:
    #5% Gehalt erhöherung für alle Mitarbeiter
    # Klassenattribut, Konstant
    ERHOEHUNGSRATE = 1.05

    #Konstruktor
    def __init__(self, name, gehalt):
        self.__name  = name
        self.__gehalt = gehalt
    
    def getName(self):
        return self.__name
    
    def getGehalt(self):
        return self.__gehalt

    #Instanzmethode, mit Objekt zu tun
    def erhoehe_gehalt(self):
        return self.__gehalt*Mitarbeiter.ERHOEHUNGSRATE

    # Statische Methode
    @staticmethod
    def ist_vollzeit(stunden_pro_Woche):
        return stunden_pro_Woche >= 40