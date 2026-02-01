roh_bestellung=[(101,2),(101,1),(102,3),(101,2),(101,10)]

katalog = {101: "T-Shirt",102: "Hose",103: "Socken"}

# bestellte_ids = set([item[0] for item in roh_bestellung])
bestellte_ids={element[0] for element in roh_bestellung}
print(bestellte_ids)

print(f"Zusammenfasung von Bestellung:")
for artikel_id in bestellte_ids:
    print(artikel_id," ",katalog[artikel_id])