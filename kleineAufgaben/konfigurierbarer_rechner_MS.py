# import math

def berechne_ergebnis(*zahlen,startwert=10, **optionnen):

    print(f"startwert = {startwert}\nZahlen = {zahlen}\nOptionnen = {optionnen} ")
    sum = startwert

    for z in zahlen:
        sum += z

    if "verdoppeln" in optionnen:
            if optionnen["verdoppeln"]==True:
                sum*=2
    if "abrunden" in optionnen:
            if optionnen["abrunden"]==True:
                sum = round(sum)
                # sum = math.ceil(sum)
    
    return sum


ergebnis = berechne_ergebnis(10.5,20.2,startwert=0,abrunden=True)
ist_über_hundert = lambda x: x>=100


print(f"Summe ist {ergebnis}. Ist das über hundert? {ist_über_hundert(ergebnis)}")

