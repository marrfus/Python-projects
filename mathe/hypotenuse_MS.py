import math

def hypotenuse(a:float | None=0 ,b:float | None=0) -> float:
    """
    Rechnet die Hypotenuse in einem\n
    rechtwinkligen Dreieck mit Kathets a und b. 
    """
    return round(math.sqrt(a**2+b**2),2)


print(hypotenuse(8,4))
     