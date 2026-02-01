from random import randint

#maximal Wert von zufällige zahl
zahl_range=6
#Zähler. Liste mit 0-elementen, zahl_range Stuck
z=[0]*zahl_range

#Durchschläufe: n
n=1000000
for i in range(n):
    # random zahl
    zahl = randint(1,zahl_range)
    # zählerzustand aktualisieren
    z[zahl-1]+=1

# Durchschnitt rechnen
# avg = sum(z)/zahl_range
avg = n/zahl_range
# Ergebnisse
print(f"Durchläufe    :    {n}\nDurchschnitt    :    {avg:.2f}")
for i in range(zahl_range):
    #differenz rechnen
    dif = z[i]-avg
    prozent = dif/avg*100
    print(f"Zähler {i+1}:  {z[i]}        Diff:  {dif:.2f}    %: {abs(prozent):.2f}")
        