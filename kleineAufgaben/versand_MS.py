def versand_rechner(bestellwert, EU, DE):
    versandkosten = 0
    print(f"Bestelltewert = {bestellwert}.\nVersand in EU? {EU}\nVersand in DE? {DE}")
    print("."*30)

    if bestellwert>=50:
        if DE:
            versandkosten = 0
        elif EU:
            versandkosten = 0
        else:
            versandkosten = 10
        
    else:
        if DE:
            versandkosten = 5
        elif EU:
            versandkosten = 7.5
        else:
            versandkosten = 12
    return versandkosten

###### Testfälle  #######
print("\n#######  Bestellwert kleiner als 50 Euro  #######\n")
print(f"Versandkosten: {versand_rechner(10, False, True )}\n\n")
print(f"Versandkosten: {versand_rechner(20, True, False)}\n\n")
print(f"Versandkosten: {versand_rechner(45, False ,False)}\n\n")

print("\n#######  Bestellwert größer oder gleich 50 Euro  #######\n")
print(f"Versandkosten: {versand_rechner(50, False, False)}\n\n")
print(f"Versandkosten: {versand_rechner(60, True, False)}\n\n")
print(f"Versandkosten: {versand_rechner(100, False, True)}\n\n")
    
        