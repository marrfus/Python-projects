from .vehicle import Vehicle

class Motorrad(Vehicle):
    def __init__(self, id:int):
        super().__init__(id)
        self.typ = "Motorrad"

     