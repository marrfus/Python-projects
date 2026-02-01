from fahrzeug import Fahrzeug

f1 = Fahrzeug("VW", "Golf", 2017, "grau")
f2 = Fahrzeug("Lamborgini", "Diablo", 1987, "rot")

f1.informationenAusgeben()
f1.starten()
print("-"*30)
print(f"{f1.model} Motorstatus: {f1.getMotorGestartet()}")

f1.fahren()
print()

f2.setFarbe("sonnig gelb")
f2.informationenAusgeben()
print("-"*30)
f2.fahren()
