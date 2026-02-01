
class Kreis:
    pi = 3.14159

    def __init__(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    @staticmethod
    def ist_positiv(wert):
        return wert >= 0
    
    @classmethod
    def aus_umfang(cls, umfang):
        return cls(umfang/(2*cls.pi))


k = Kreis(10)

k2 = Kreis.aus_umfang(25)

print(k2.getRadius())
print(k.getRadius())
print(Kreis.ist_positiv(-20))
print(Kreis.aus_umfang(25).getRadius())