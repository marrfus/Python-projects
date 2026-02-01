l=[]

def quersumme(n):           
    if n==0:
        return 0        
    else:        
        return n%10 +quersumme(n//10)
    
def collatz(n):
    global l
    if n==1:
        l.append(n)
        return l
    elif n%2==0:
        l.append(n)
        return collatz(n//2)
    else:
        l.append(n)
        return collatz(3*n +1)

qs=2019
cf=5
print(f"Die Quersumme von {qs} ist {quersumme(qs)}")
print("-"*30)
print(f"Collatz-Folge von {cf}:")
print(*collatz(cf))
       