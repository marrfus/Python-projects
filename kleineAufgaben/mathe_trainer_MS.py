from random import randint
from random import choice

  
    
##########  Teil 1 (Mathe Trainer)   ############

# eingabe = input("Wie viele Übungen möchtest du machen?")
# while not eingabe.isdigit() or (eingabe.isdigit() and not (0<int(eingabe)<=100)):
#     eingabe = input("Gib bitte die Echtezahl zwischen 1 und 100 ein!")
# for i in range (0,int(eingabe),1):
#     o = choice('+-*')
#     a = randint(1,10)
#     b = randint(1,10)
   
#     uebung=f"{a}{o}{b}" 
#     erg=eval(uebung)
#     ans = input(uebung+"= ?")
#     if ans==str(erg):
#         print(f"Ja, das ist richtig!")
#     else:
#         print(f"Leider falsch. Die korrekte Antwort lautet: {erg}")




# ############## Optional (+ Boolean)   ###########
# def mach_aufgabe():
#     o = choice(['+','-','*','>','<','=='])
#     a = randint(1,10)
#     b = randint(1,10)
#     return f"{a} {o} {b}" 

# def output(ergebnis,answer):
#     if answer==str(ergebnis):
#         print(f"Ja, das ist richtig!")
#     else:
#         print(f"Leider falsch. Die korrekte Antwort lautet: {ergebnis}")



# eingabe = input("Wie viele Übungen möchtest du machen?")

# while not eingabe.isdigit() or (eingabe.isdigit and not (0<int(eingabe)<=100)):
#     eingabe = input("Gib bitte die Echtezahl zwischen 1 und 100 ein!")

# for i in range (0,int(eingabe),1):
#     uebung = mach_aufgabe()
#     erg=eval(uebung)    
#     ans = input(uebung+"= ?\n")
#     if type(erg)==bool:
#         while (ans!="Wahr" and ans!="Falsch"):
#             ans = input("Schreib bitte Wahr oder Falsch.\n")
#         if erg:
#             erg="Wahr"
#         else:
#             erg="Falsch"
       
#     output(erg,ans)



############## Optional zum kniffeln (+ Bin)   ###########
def mach_aufgabe():
    is_bin=False
    o = choice(['+','-','*','>','<','==','|','&'])

    if o in ['|','&']:
        is_bin=True
        a = bin(randint(1,10))
        b = bin(randint(1,10))
        return f"{a} {o} {b}",is_bin

    a = randint(1,10)
    b = randint(1,10)
    return f"{a} {o} {b}",is_bin



def output(ergebnis,answer,is_bin,fail):    
    if is_bin:
        ergebnis=bin(ergebnis)
    if fail:
        print(f"Ohh, Schade, dass du aufgegeben hast. Die korrekte Antwort war: {ergebnis}\n")
        return
    if answer==str(ergebnis):
        print(f"Ja, das ist richtig!\n")
    else:
        print(f"Leider falsch. Die korrekte Antwort lautet: {ergebnis}\n")



eingabe = input("Wie viele Übungen möchtest du machen?")

while not eingabe.isdigit() or (eingabe.isdigit() and not (0<int(eingabe)<=100)):
    #eingabe.isalnum() #benutzen für float zu holen
    eingabe = input("Gib bitte die Echtezahl zwischen 1 und 100 ein!")

for i in range (0,int(eingabe),1):
    nicht_gemacht=False
    uebung, ist_bin = mach_aufgabe()
    erg=eval(uebung)    
    ans = input(uebung+" = ?\n")
    if type(erg)==bool:
        while (ans!="w" and ans!="f"):
            if ans=="quit":
                print("-"*10+"  übergesprungene Aufgabe  " + "-"*10)
                nicht_gemacht=True
                break
            ans = input("Schreib bitte w (für Wahr) oder f (für Falsch).\nSchreib \"quit\" um diese Eingabeschleife zu beenden\n")
        if erg:
            erg="w"
        else:
            erg="f"
    if ist_bin: 
        while (not ans.startswith("0b") or (ans.startswith("0b") and len(ans)>10)):
            if ans=="quit":
                print("-"*10+"  übergesprungene Aufgabe  " + "-"*10)
                nicht_gemacht=True
                break
            ans = input('Fäng bitte dein Antwort mit "0b" an: binäre Darstellung.\nAchte auch auf die Wertlänge: es sollte maximal 8 Stellen lang sein.\nSchreib "quit" um diese Eingabeschleife zu beenden\n')        

    output(erg,ans,ist_bin,nicht_gemacht)