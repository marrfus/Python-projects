def F_folge(n):
    fibo_list=[0,1]
    for i in range(2,n):
      fibo_list.append(fibo_list[i-2]+fibo_list[i-1])
    return fibo_list   

while True:
    try:
        laenge = int(input(f"Wie lange soll Fibonacci-Folge sein?  "))
        if laenge>2:
            break
        else: raise Exception("Gib bitte ein Zahl größer als 2 ")
    except ValueError as e:
        print("Es muss eine Zahl sein! ",e)
    except Exception as e:
        print(e)

print(F_folge(laenge))