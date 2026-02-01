milch_bestand = 15.75
kaffee_packungen = 32
zukerwürfel = 1023
budget = 250
liferanten= ["Milch-Express", "Bohnen-Co", "Süß-GmbH"]

#Nachschub Kalkulation
print(f"Wir können {milch_bestand//5} volle kanister Milch fühlen.")
print(f"Teoretische berechnung 32^1.05 = {32**1.05:.2f}")
milch_bestand+=4.5
print(f"Aktualisierte Milchmenge ist {milch_bestand}")

#2.Bestell Entscheidungen
print(f"Muss Milch nachbestellt werden? {milch_bestand<15}")
print(f"Haben wir genau 32 Kaffeepackungen? {kaffee_packungen==32}")
print(f"Muss sowohl Milch als auch Kaffee nachbestellt werden? {milch_bestand<15 and kaffee_packungen<10}")
print(f"Wird Bestellung ausgelöst? {not budget<100}")

#3. Effizienz und Identität
print(f'Ist Lieferant "Süß-GmbH" in der Liste? {"Süß-GmbH" in liferanten}')
budget_copy = budget
print(f"Sind Budget und Budget_copy dieselbe? {budget is budget_copy}")

#4. Zuker-Optimierung
print(f"Zukerwürfel>>1 = {zukerwürfel>>1}") #Wir haben 1 Zukerwürfel verloren
