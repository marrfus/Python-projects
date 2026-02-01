
a=0
b=0
ergebnis=0


def plus(x,y):
   return x + y
 

def minus(x,y):
   return x - y

def mal(x,y):
   return x * y

def div(x,y):
   if y==0:
      print ('Man darf nicht an 0 dividieren!')
      return "unmöglich"
   return x / y

def main():
   a=input('Lass uns rechnen! Gib mir bitte die erste Zahl.\n')
   b=input('Gib mir bitte die zweite Zahl.\n')
   aktion = input('Gib mir bitte die Aktion: + - * /\n')

   a = float(a)
   b = float(b)

   if(aktion=='+'):
       ergebnis = plus(a, b)
   if(aktion == '-'): 
        ergebnis = minus(a, b)
   if(aktion == '*'): 
        ergebnis = mal(a, b)
   if(aktion == '/'):
        ergebnis = div(a, b)

   print("Das Ergebnis von ", a , aktion , b , " ist " , ergebnis)

main()