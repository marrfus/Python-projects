
a=float(input("Gib bitte a: "))
b=float(input("Gib bitte b, b sollte kleiner als a sein: "))
c=a-b
while c!=0:
    c=a-b
    if c==0:
        print(f"a = {a}")
        break
    else:
        if c>=b:
            a=c
        else:
            b=c

