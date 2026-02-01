
def recurse_sum(n):
    if n<2:
        return n
    else:
        return n+recurse_sum(n-1)

def recurse_fibo(n):
    if n<2:
        return n
    else:
        return recurse_fibo(n-1)+recurse_fibo(n-2)


n=10
print(f"Summe von {n} natürliche Zahlen ist {recurse_sum(n)}")
print(f"Fibonacci F(n) von n = {n}  ist: {recurse_fibo(n)}")
print("Fibonacci-Folge fängt von 0 an: F(0)=0, F(10)=55")
