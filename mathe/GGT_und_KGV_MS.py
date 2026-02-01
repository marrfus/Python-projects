

def primfaktorzerlegung(n):
 
 """
 Zerlegt eine Zahl in ihre Primfaktoren und deren Exponenten.
 Gibt ein Dictionary {Primfaktor: Exponent} zurück.
 """
 faktoren = {}
 teiler = 2 # Starte mit der kleinsten Primzahl
 # Schleife solange der Teiler nicht größer ist als der Rest von n
 while teiler * teiler <= n:
        while n % teiler == 0:
        # Wenn n durch den Teiler teilbar ist, erhöhe den Exponenten
            faktoren[teiler] = faktoren.get(teiler, 0) + 1
            n //= teiler # Teile n durch den Faktor
        teiler += 1 # Gehe zum nächsten möglichen Teiler
    # Wenn nach der Schleife n noch > 1 ist, ist der verbleibende Rest selbst eine Primzahl
 if n > 1:
    faktoren[n] = faktoren.get(n, 0) + 1
 return faktoren


def ggt_durch_pfz(a, b):
    ggt_wert=1
    prim_a = primfaktorzerlegung(a)
    prim_b = primfaktorzerlegung(b)
    print(f"{a} : {prim_a}\n{b} : {prim_b}")
    for key, wert in prim_a.items():
        if key in prim_b:
            if prim_a[key] > prim_b[key]:
                ggt_wert=ggt_wert*key**prim_b[key]
            else:
                ggt_wert=ggt_wert*key**prim_a[key]
    return ggt_wert


def kgv_durch_pfz(a, b):
    kgv_wert=1
    prim_a = primfaktorzerlegung(a)
    prim_b = primfaktorzerlegung(b)
    for key, wert in prim_a.items():
        if key in prim_b:
            if prim_a[key] > prim_b[key]:
                kgv_wert=kgv_wert*key**prim_a[key]
            else:
                kgv_wert=kgv_wert*key**prim_b[key]
    return kgv_wert


a=input("Gib erste Zahl:  ")
b=input("Gib zweite Zahl:  ")
print(f"GGT = {ggt_durch_pfz(int(a),int(b))}")
print(f"KGV = {kgv_durch_pfz(int(a),int(b))}")
