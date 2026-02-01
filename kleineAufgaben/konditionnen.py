#Ohmschen Gesetz

eingabe = input("Was rechnen wir? R, I oder U: ")
if eingabe=="R":
    print("Es ist Wiederstand. R = U/I")
    I = int(input("Ich brauche zwei Werte: I und U.\nI = "))
    U = int(input("U = "))
    print(f"R = {U/I:.2f} \u03A9")
elif eingabe=="I":
    print("Es ist Strom. I = U/R")
    U = int(input("Ich brauche zwei Werte: U und R.\nU = "))
    R = int(input("R = "))
    print(f"I = {U/R:.2f} A")
elif eingabe=="U":
    print("Es ist Spannung. U = R*I")
    R = int(input("Ich brauche zwei Werte: R und I.\nR = "))
    I = int(input("I = "))
    print(f"U = {I*R} V")
else:
    print("Sie haben was falsches gedrückt. Ich kann nur R, I oder U rechnen.\nStarten Sie bitte nochmal.")


# #Body Mass Index
# gewicht = float(input("Gib mir bitte dein Körpergewicht in kg ein: "))
# grosse = float(input("Gib mir bitte deine Körpergroße in cm ein: "))/100
# geschlecht = input("Gib bitte dein geschlecht m/w ein: ")
# print("-"*30)
# BMI = round(gewicht/grosse**2,1)
# print(f"Dein BMI = {BMI}")
# print("Deine BMI-Klassifikation:")
# if geschlecht=="m":
#     if BMI<20:
#         print("Untergewicht")
#     elif BMI>=20 and BMI<25:
#         print("Normalgewicht")
#     elif BMI>=25 and BMI<30:
#         print("Übergewicht")
#     elif BMI>=30 and BMI<40:
#         print("Adipositas")
#     else:
#         print("massive Adipositas")
# elif geschlecht=="w":    
#     if BMI<19:
#         print("Untergewicht")
#     elif BMI>=19 and BMI<24:
#         print("Normalgewicht")
#     elif BMI>=24 and BMI<30:
#         print("Übergewicht")
#     elif BMI>=30 and BMI<40:
#         print("Adipositas")
#     else:
#         print("massive Adipositas")
# else:
#     print("Du hast falsches Geschlecht eingedrückt. Mach von Anfang.")





