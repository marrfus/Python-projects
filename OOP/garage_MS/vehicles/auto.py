
from .vehicle import Vehicle

class Auto(Vehicle):
    def __init__(self, id:int, platz:int=None, etage:int=None):
        super().__init__(id)
        self.typ = "Auto"

