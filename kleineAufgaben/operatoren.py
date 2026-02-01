#arithmetische operatoren
print("\n1. Arithmetische Operatoren.")
a=15*4
print(f"Produkt von 15 und 4 ist {a}")
a=27//5
print(f"Ganzzahl von 27/5 ist {a}")
a=27%5
print(f"Rest der Division aus 27 durch 5 ist {a}")
a=4**3
print(f"4 hoch 3 ist {a}")
print("-"*30,"\n")
 
#relationale operatoren
print("2. Relationale Operatoren.")
a=(10>=10)
print(f"Ist 10 >= 10? {a}")
a=('Apfel'!='apfel')
print(f"Ist \'Apfel\' != \'apfel\'? {a}")
a=(5<5)
print(f"Ist 5 < 5? {a}")
str="Python"
a=(len(str)==6)
print(f"Ist die Länge des Strings \"Python\" gleich 6? {a}")
print("-"*30,"\n")
 
#Zuweisungsoperatoren
print("3. Zuweisungsoperatoren.")
x=12
print(f"x={x}")
x+=3
print(f"x={x}")
x-=5
print(f"x={x}")
x*=2
print(f"x={x}")
x//=4
print(f"x={x}")
print("-"*30,"\n")
 
#logische operatoren 
print("4. Logische Operatoren.")
a = True
b = False
print(f"{a} UND {b} = {a and b}")
print(f"{a} ODER {b} = {a or b}")
print(f"NICHT {b} = {not b}")
print(f"({a} UND NICHT {b}) ODER {b} = {(a and not b) or b}")
print("-"*30,"\n")

#mitglidschaftsoperatoren
print("5. Mitgliedschaftsoperatoren")
meine_liste = [10,20,30,40]
text = "Hallo Welt"
print(f"meine_liste: {meine_liste}")
print(f"text: {text}")
a = 20 in meine_liste
print(f"Ist 20 in meiner Liste? {a}")
a = 50 not in meine_liste
print(f"Ist 50 nicht in meiner Liste? {a}")
a = "Welt" in text
print(f"Ist der Substring \"Welt\" in text? {a}")
a = "hallo" in text
print(f"Ist der Substring \"hallo\" in text? {a}")
print("-"*30,"\n")

#identitätsoperatoren
print("6. Identitätsoperatoren")
x=10
y=10
z=20
print(f"x={x}, y={y}, z={z}")
a = x is y
print(f"Ist x is y? {a}")
a = x is not z 
print(f"Ist x is not z? {a}")
a=[1,2]
b=[1,2]
c=a is b
print(f"Ist a is b? {c}")
print("-"*30,"\n")

#bitweise operatoren
print("7. Bitweise Operatoren.")
A=5
B=3
print(f"A={A}=0101\nB={B}=0011")
print(f"A & B = {A&B}")
print(f"A | B = {A|B}")
print(f"A ^ B = {A^B}")
print(f"A >> 1 = {A>>1}")