a=0
b=0
ergebnis=0


def aufgabe(x,y,z):
   if(z=='+'):
     return x+y
   elif(z=='-'):
      return x-y
   elif(z=='*'):
      return x*y
   elif(z=='/'):
      if(b==0):
         print ('Man darf nicht an 0 dividieren!')
         return "unmöglich"
      return x/y
   else:
      print ("Du hast etwas falsch gegeben. Mach nochmal.")

def main():
   a=input('Lass uns rechnen! Gib mir bitte die erste Zahl.\n')
   b=input('Gib mir bitte die zweite Zahl.\n')
   aktion = input('Gib mir bitte die Aktion: + - * /\n')

   a = float(a)
   b = float(b)

   aufgabe(a,b,aktion)

main()