

def primz(n):
    i=2
    antw_liste=[]
    while n>1:
        while n%i==0:
            antw_liste.append(i)
            n=n/i
        if i==2:
            i+=1
        else:
            i+=2
    if n!=1:
        antw_liste.append(int(n))
    return antw_liste


eingabe=input("Gib bitte Ganzzahl >0:   ")
while not eingabe.isdigit() or (eingabe.isdigit() and int(eingabe)<=0):
    eingabe=input("Ich nehme nur Echtezahlen > 0!!!    ")

eingabe=int(eingabe)
antw = primz(eingabe)

print(f"{eingabe} = {antw}")
