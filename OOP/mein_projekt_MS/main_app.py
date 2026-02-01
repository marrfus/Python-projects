from kunden_sys import add_kunde,zeige_info, kunden

kunde1= zeige_info(356, "Rayen", "r@info.com")
kunde2 = zeige_info(54, "Daria", "d@info.com")

add_kunde(kunde1)
add_kunde(kunde2)

for k in kunden:
    print(k)