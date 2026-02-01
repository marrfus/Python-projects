
def berechne_versandkosten(laenge_cm, gewicht_kg):
    if laenge_cm<0 or gewicht_kg<0:
        print("Ungültige Wert! Das Gewicht und die Länge müssen positiv sein.")
        return 0
    match laenge_cm:
        case l if l>200 or gewicht_kg>20:
            print(f"Versandklasse: Spezialgut\nVersandkosten: \u20AC{25+1.5*gewicht_kg}")
        case l if l<30:
            print(f"Versandklasse: Kleinsendung\nVersandkosten: \u20AC{2.5+0.5*gewicht_kg}")
        case l if l<=100:
            print(f"Versandklasse: Standartsendung\nVersandkosten: \u20AC{5+0.8*gewicht_kg}")
        case l if l<=200:
            print(f"Versandklasse: Großpaket\nVersandkosten: \u20AC{10+1.2*gewicht_kg}")
        case _:
            print("Fehler in match-case")


def main():
    l=float(input("Länge des Paketes, cm: "))
    g=float(input("Gewicht des Paketes, kg: "))
    print("."*30)
    berechne_versandkosten(l,g)


main()

    