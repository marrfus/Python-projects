def ob_schaltjahr(jahr):    
    #durch 4
    if jahr%4==0:
        #durch 100
        if jahr%100==0:
            #durch 400
            if jahr%400==0:
                return f"Schaltjahr. R1: Ausnahme durch 400. J J J"  # J J J
            else:
                return f"Kein Schaltjahr. R2: Ausnahme durch 100, aber nicht durch 400. J J N"  # J J N
        else: return f"Schaltjahr. R4:  J N N"  # J N N
    else: return f"Kein Schaltjahr.  R8:  N N N" # N N N
    



# Gültig sind nur R1, R2, R4 und R8
ans = None
while ans!="q":
    ans=input('\nint Jahr oder "q" für quit:     ')
    if ans.isdigit() and 1500<=int(ans)<=2108:
        print(ob_schaltjahr(int(ans)))
    else: print("Fehler! Jahr muss int sein und in range 1500-2108!")