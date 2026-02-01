
def inv_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]["Menge"] > a[j+1]["Menge"]:
                tausch(a,j)
            if a[j]["Menge"] == a[j+1]["Menge"] and a[j]["Preis"] < a[j+1]["Preis"]:
                tausch(a,j)
            if a[j]["Menge"] == a[j+1]["Menge"] and a[j]["Preis"] == a[j+1]["Preis"] and a[j]["Name"] > a[j+1]["Name"]:
                tausch(a,j)



def tausch(a,j):
    a[j],a[j+1] = a[j+1],a[j]


inventar = [
{"Name": "Axt", "Preis": 25.50, "Menge": 10},
{"Name": "Hammer", "Preis": 12.99, "Menge": 50},
{"Name": "Säge", "Preis": 25.50, "Menge": 5},
{"Name": "Schraubendreher", "Preis": 5.00, "Menge": 50},
{"Name": "Bohrer", "Preis": 79.99, "Menge": 2},
{"Name": "Zange", "Preis": 12.99, "Menge": 15}
]

inv_sort(inventar)
print(f"Ergebnis: ")
for i in range (len(inventar)):
    print(inventar[i])