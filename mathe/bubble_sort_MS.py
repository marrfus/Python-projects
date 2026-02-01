

def BubbleSort(a):
    i = len(a)-1
    while i>0:
        j=1
        while j<=i:
            if a[j-1]>a[j]:
                tausche(a,j)
            j+=1
        print(f"{i}: {a}")
        i-=1

def tausche(a,j):
    a[j-1], a[j] = a[j], a[j-1]
    # temp = a[j-1]
    # a[j-1] = a[j]
    # a[j] = temp
    

a = [7, 4, 12, 1, 2]
print(f"a: {a}")
print("-"*20)

BubbleSort(a)
print(f"\nErgebnis:    {a}")