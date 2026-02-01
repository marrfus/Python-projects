
from fahrzeug import Fahrzeug

class Auto(Fahrzeug):

    def __init__(self, marke, geschwindigkeit, anzahl_tueren):
        super().__init__(marke, geschwindigkeit)
        self.__anzahl_tueren = anzahl_tueren

    # Override
    def beschleunigen(self,wert:int):
        # super().beschleunigen(wert)
        self.geschwindigkeit += wert
        return f"Das Auto {self.marke} beschleunigt."

    @staticmethod
    def zulasungsinformation():
        return f"Alle Autos benötigen eine gültige Zulassung."