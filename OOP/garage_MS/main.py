
from vehicles import Vehicle,Parkhaus




a1 = Vehicle("WES93QK","Auto")
a2 = Vehicle("MW 5478","Motorrad")
a3 = Vehicle("KO 6543","Auto")

ph = Parkhaus(3,5)
print(f"Parkhaus Kapazität: {ph.getKapazitaet()}")
print(ph.parkVehicle(a1.id,a1.type))
print(ph.getPosition(a1.id))
print(f"Geparkte Fahrzeuge: ")
print(ph.parkVehicle(a2.id,a2.type))
print(ph.parkVehicle(a3.id,a3.type))
ph.getVisual()
# print(*ph.besetzt)
print(ph.unparkVehicle(a1.id))
ph.getVisual()
print(ph.unparkVehicle(a2.id))
print(ph.parkVehicle(a2.id,a2.type))
ph.getVisual()
ph.unparkVehicle(a2.id)
ph.unparkVehicle(a3.id)
ph.parkVehicle(a1.id,a1.type)
ph.parkVehicle(a2.id,a2.type)

ph.getVisual()

