

def verarbeite_daten(*daten, methode=None):
    print(f"Daten: {daten}, Methode: {methode}")
    if methode:       
        return list(map(methode,daten))
    return daten

#Testfälle
print("Test 1: Liste[1,2,3] ohne methode")
print(f"Ergebnis: {verarbeite_daten(1,2,3)}\n")

print("Test 2: Liste[4,5,6] und die methode als Lambda, die jede Zahl quadriert.")
print(f"Ergebnis: {verarbeite_daten(4,5,6,methode=lambda x:x**2)}\n")

print("Test 3: Liste[10,25,40] und die methode als Lambda, die jede Zahl durch 5 teilt und das Ergebnis um 1 subtrahiert.")
print(f"Ergebnis: {verarbeite_daten(10,25,40,methode=lambda x:x/5-1)}\n")

